# 🧠 Diabetes Prediction using Machine Learning

This is a machine learning web application that predicts the likelihood of diabetes in a patient based on medical attributes. It uses a trained **Random Forest Classifier** on the **Pima Indians Diabetes Dataset** and is deployed using Flask.

---

## 🚀 Live Demo

👉 [View Live App](https://your-deployed-url.onrender.com)

---

## 📊 Model Performance

- **Best Model:** Random Forest Classifier
- **Cross-Validation Accuracy:** `0.7683 ± 0.0304`
- **Accuracy on Test Set:** `0.7532`

### 🔍 Classification Report:
| Metric     | Class 0 | Class 1 |
|------------|---------|---------|
| Precision  | 0.81    | 0.65    |
| Recall     | 0.80    | 0.67    |
| F1-Score   | 0.81    | 0.66    |
| Support    | 99      | 55      |

- **Overall Accuracy:** 75.3%
- **Macro Avg F1:** 0.73
- **Weighted Avg F1:** 0.75

---

## 🧰 Tech Stack

- **Backend:** Python, Flask, scikit-learn, NumPy, joblib
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render
- **Model:** RandomForestClassifier

---

## 🗂️ Project Structure

<pre> ├── app.py # Main Flask application<br> ├── model/<br> │ └── diabetes_model1.pkl # Trained ML model file<br> ├── templates/<br> │ └── index.html # Frontend HTML template<br> ├── static/ <br> │ ├── style.css # Custom CSS styling <br> │ └── script.js # JavaScript for form handling<br> ├── requirements.txt # List of Python dependencies<br> ├── Procfile # For deployment with Render <br> ├── .gitignore # Files to be ignored by Git<br> └── README.md # Project documentation </pre>


---

## ⚙️ How to Run Locally

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/diabetes-predictor.git
cd diabetes-predictor


📬 API Usage
Send a POST request to /predict with JSON data like:
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 25,
  "Insulin": 85,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.25,
  "Age": 24
}
Response:
{
  "prediction": 0,
  "probability": 0.1742
}
