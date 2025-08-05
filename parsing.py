import pandas as pd
from feature_extraction import extract_features_common, feature_names
import joblib

def extract_features(url, url_type): # Wrapper for training data
    print(f"Processing URL: {url}")
    features = extract_features_common(url)
    features['type'] = 1 if str(url_type) == 'benign' else 0
    return features

if __name__ == "__main__":
    df = pd.read_csv("malicious_phish.csv") 
    
    df = df.dropna(subset=["url"]) # Drop any lines without a URL
    df = df.dropna(subset=["type"]) # Drop any lines without a type
    df = df[df['type'].isin(['benign', 'defacement'])]

    features = df.apply(lambda row: extract_features(row["url"], row["type"]), axis=1).apply(pd.Series)

    final_df = pd.concat([df["url"], features], axis=1)
    final_df.to_csv("features.csv", index=False)
    print("Feature extraction complete! Saved to 'features.csv'")

    joblib.dump(feature_names, "feature_names.pkl")
    print("Feature names saved to 'feature_names.pkl'")