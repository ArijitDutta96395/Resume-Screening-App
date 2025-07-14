def clean_resume(text):
    # Dummy cleaner (just returns lowercased text for now)
    return text.lower()

def predict_category(text):
    # Dummy predictor (for testing only)
    # Later you’ll replace this with your actual ML model.
    if "network" in text:
        return "Network Security Engineer"
    else:
        return "General Category"
