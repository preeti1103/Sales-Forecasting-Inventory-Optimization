from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the forecasting model
model = joblib.load(r'C:\Users\preet\Documents\MyProjects\Sales-Forecasting-Inventory-Optimization\models\sales_forecasting_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    steps = data.get('steps', 1)  # Number of steps to forecast

    # Generate predictions
    predictions = model.forecast(steps=steps)

    # Return the predictions as JSON
    return jsonify({'predictions': predictions.tolist()})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)