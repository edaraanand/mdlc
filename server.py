import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model (ensure this matches where the model is saved)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Ensure input data is in the right shape (e.g., 4 features for the Iris dataset)
    input_data = np.array(data['features']).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the result as a JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
