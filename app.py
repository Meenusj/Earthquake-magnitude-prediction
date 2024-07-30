from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the model
model_path = 'random_forest_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Initialize Flask application
app = Flask(__name__)

# Initialize the scaler (fit it with sample data for the purpose of this example)
scaler = StandardScaler()
sample_data = np.array([[0, 0, 0, 0, 0, 0]])  # Replace with appropriate sample data
scaler.fit(sample_data)

# Define home route
@app.route('/')
def home():
    return render_template('index.html')

# Define predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form submission
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        depth = float(request.form['depth'])
        horizontalError = float(request.form['horizontalError'])
        depthError = float(request.form['depthError'])
        magError = float(request.form['magError'])

        # Prepare feature array for model prediction
        features = np.array([[latitude, longitude, depth, horizontalError, depthError, magError]])

        # Scale features
        features_scaled = scaler.transform(features)

        # Predict magnitude
        prediction = model.predict(features_scaled)[0]

        # Return prediction
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return render_template('result.html', error=str(e))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
