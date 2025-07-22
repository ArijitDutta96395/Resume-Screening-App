import pickle
import re

# === Load Models ===
with open("models/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)
with open("models/clf.pkl", "rb") as f:
    clf_model = pickle.load(f)
with open("models/encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# === Resume Cleaning Function ===
def clean_resume(txt):
    clean_text = re.sub(r"http\S+\s*", " ", txt)
    clean_text = re.sub(r"RT|cc", " ", clean_text)
    clean_text = re.sub(r"#\S+\s*", " ", clean_text)
    clean_text = re.sub(r"@\S+", " ", clean_text)
    clean_text = re.sub(r"[%s]" % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), " ", clean_text)
    clean_text = re.sub(r"[^\x00-\x7f]", " ", clean_text)
    clean_text = re.sub(r"\s+", " ", clean_text)
    return clean_text.strip().lower()

# === Prediction Function ===
def predict_category(text):
    cleaned = clean_resume(text)
    vectorized = tfidf.transform([cleaned])
    prediction = clf_model.predict(vectorized)
    category = label_encoder.inverse_transform(prediction)
    return category[0]

# === Debugging Info ===
if __name__ == "__main__":
    sample_text = """
    John Doe is an experienced Network Security Engineer with over 7 years of expertise in designing, implementing, and managing network security infrastructures.
    He is proficient in deploying firewalls, intrusion detection systems (IDS), VPNs, and network monitoring tools.
    Certifications include CISSP, CEH, and CCNA.
    """

    print("=== Original Resume Text ===\n")
    print(sample_text.strip())

    print("\n=== Cleaned Resume Text ===\n")
    print(clean_resume(sample_text))

    print("\n=== Available Categories in Model ===\n")
    print(label_encoder.classes_)

    result = predict_category(sample_text)
    print("\n=== Predicted Category ===\n")
    print(result)
