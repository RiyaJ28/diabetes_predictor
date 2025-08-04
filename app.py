from flask import Flask, request,jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('./model/diabetes_model1.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data from frontend
        data = request.json

        # Extract features in correct order (example: 8 features from Pima dataset)
        features = [
            data['Pregnancies'],
            data['Glucose'],
            data['BloodPressure'],
            data['SkinThickness'],
            data['Insulin'],
            data['BMI'],
            data['DiabetesPedigreeFunction'],
            data['Age']
        ]

        # Convert to NumPy array and reshape for model
        input_array = np.array(features).reshape(1, -1)

        # Predict
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1]

        result = {
            "prediction": int(prediction),  # 0 or 1
            "probability": round(float(probability), 4)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
