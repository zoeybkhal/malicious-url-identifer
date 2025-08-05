from flask import Flask, request, render_template
import joblib
from feature_extraction import extract_features_common, feature_names

# Load the trained model
model, _ = joblib.load("url_model.pkl")

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        url = request.form['url']
        
        features_dict = extract_features_common(url)
        features_list = [features_dict.get(feat, 0) for feat in feature_names]

        print("Final features list used for prediction:")
        print(features_list)

        prediction_value = model.predict([features_list])[0]
        prediction = "This URL is likely benign ✅" if prediction_value == 1 else "This URL is likely malicious ❌"
    
    return render_template('index.html', prediction=prediction)
        
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    

    
    

   
