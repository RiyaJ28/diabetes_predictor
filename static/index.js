document.getElementById('diabetes-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = parseFloat(value);
  });

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    if (response.ok) {
      document.getElementById('result').innerHTML = `
        Prediction: <strong>${result.prediction === 1 ? "Diabetic" : "Non-Diabetic"}</strong><br>
        Probability: <strong>${result.probability}</strong>
      `;
    } else {
      document.getElementById('result').textContent = "Error: " + result.error;
    }
  } catch (error) {
    document.getElementById('result').textContent = "Network error: " + error.message;
  }
});
