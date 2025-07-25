from flask import Flask, request, jsonify, render_template
from pycaret.regression import load_model, predict_model
import pandas as pd

app = Flask(__name__)

# Load trained PyCaret model
model = load_model('insurance_claim_model')

@app.route('/')
def home():
    return render_template('index.html')  # You’ll create this HTML file next

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form (assuming form fields match your model's input columns)
        input_data = {
            'age': request.form['age'],
            'sex': request.form['sex'],
            'weight': request.form['weight'],
            'bmi': request.form['bmi'],
            'hereditary_diseases': request.form['hereditary_diseases'],
            'no_of_dependents': int(request.form['no_of_dependents']),
            'smoker': int(request.form['smoker']),
            'city': request.form['city'],
            'bloodpressure': request.form['bloodpressure'],
            'diabetes': int(request.form['diabetes']),
            'regular_ex': int(request.form['regular_ex']),
            'job_title': request.form['job_title']
        }

        df = pd.DataFrame([input_data])
        prediction = predict_model(model, data=df)
        output = round(prediction.loc[0, 'prediction_label'], 2)

        return render_template('index.html', prediction_text=f'Estimated Claim Amount: ${output}')
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
