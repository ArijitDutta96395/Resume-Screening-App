import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# ✅ 1. Load Dataset
df = pd.read_csv("UpdatedResumeDataSet.csv")

# ✅ 2. Clean Resumes (Reuse your function)
def clean_resume(txt):
    clean_text = re.sub(r'http\S+\s', ' ', txt)
    clean_text = re.sub(r'RT|cc', ' ', clean_text)
    clean_text = re.sub(r'#\S+\s', ' ', clean_text)
    clean_text = re.sub(r'@\S+', ' ', clean_text)
    clean_text = re.sub(r'[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text

df['Resume'] = df['Resume'].apply(lambda x: clean_resume(x))

# ✅ 3. Encode Target Labels
le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])

# ✅ 4. TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(df['Resume'])
X = tfidf.transform(df['Resume'])
y = df['Category']

# ✅ 5. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ 6. Train Classifier
svc_model = OneVsRestClassifier(SVC())
svc_model.fit(X_train, y_train)

# ✅ 7. Evaluate (optional)
y_pred = svc_model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

# ✅ 8. Save Models (IMPORTANT STEP)
pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(svc_model, open("clf.pkl", "wb"))
pickle.dump(le, open("encoder.pkl", "wb"))

print("✅ Model Training & Saving Completed.")
