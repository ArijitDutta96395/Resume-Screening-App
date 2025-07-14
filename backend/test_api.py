import requests
import os

url = "http://localhost:8000/upload_resume/"
file_path = os.path.join(os.path.dirname(__file__), "sample_resume.txt")

with open(file_path, "rb") as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:", response.json())
