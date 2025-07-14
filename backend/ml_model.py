import pickle
import re

# Load models once at startup
with open("models/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)
with open("models/clf.pkl", "rb") as f:
    clf_model = pickle.load(f)
with open("models/encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def clean_resume(txt):
    clean_text = re.sub('http\S+\s', ' ', txt)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+\s', ' ', clean_text)
    clean_text = re.sub('@\S+', ' ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def predict_category(text):
    cleaned = clean_resume(text)
    vectorized = tfidf.transform([cleaned])
    vectorized = vectorized.toarray()
    prediction = clf_model.predict(vectorized)
    category = label_encoder.inverse_transform(prediction)
    return category[0]
