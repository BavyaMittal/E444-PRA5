from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
imporr os

application = Flask(__name__)

# Load the pre-trained model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), 'basic_classifier.pkl')
with open(model_path, 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer_path = os.path.join(os.path.dirname(__file__), 'count_vectorizer.pkl')
with open(vectorizer_path, 'rb') as vd:
    vectorizer = pickle.load(vd)

# Load model and vectorizer when the application starts
model, vectorizer = load_model()

@application.route('/')
def home():
    return "Hello, welcome to Fake News Detection API"

# Define a route for sentiment prediction
@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'GET'
        return "Use POST method"
    
    try: 
        data = request.get_json()  # Receive JSON data
        
        if not data: 
                return jsonify ({'error': 'No input'}), 400
        
        print (f"Input: {data}")
        
        predictions = []
        for i in data: 
            vectorized_input = vectorizer.transform([i])
            prediction = loaded_model.predict(vectorized_input)[0]

            if prediction =='FAKE': 
                predictions.append(1)
            
            elif prediction = 'REAL': 
                predictions.append(0)
            
            else: 
                raise ValueError(f"Unexpected prediction value: {prediction}")
            
        print ("Prediction:", predictions)

        return jsonify({'input': data,'prediction': predictions}), 200

if __name__ == '__main__':
    app.run(debug=True)
