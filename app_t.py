from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def validate_input(data):
    """Validate form input data."""
    try:
        # Convert numeric fields and check ranges
        data['age'] = float(data['age'])
        if not 18 <= data['age'] <= 100:
            return False, "Age must be between 18 and 100."
        
        data['weight'] = float(data['weight'])
        if not 30 <= data['weight'] <= 300:
            return False, "Weight must be between 30 and 300."
        
        data['bmi'] = float(data['bmi'])
        if not 10 <= data['bmi'] <= 50:
            return False, "BMI must be between 10 and 50."
        
        data['bloodpressure'] = float(data['bloodpressure'])
        if not 80 <= data['bloodpressure'] <= 200:
            return False, "Blood pressure must be between 80 and 200."
        
        data['no_of_dependents'] = int(data['no_of_dependents'])
        if not 0 <= data['no_of_dependents'] <= 10:
            return False, "Number of dependents must be between 0 and 10."
        
        data['smoker'] = int(data['smoker'])
        if data['smoker'] not in [0, 1]:
            return False, "Smoker must be 0 or 1."
        
        data['diabetes'] = int(data['diabetes'])
        if data['diabetes'] not in [0, 1]:
            return False, "Diabetes must be 0 or 1."
        
        data['regular_ex'] = int(data['regular_ex'])
        if data['regular_ex'] not in [0, 1]:
            return False, "Regular exercise must be 0 or 1."
        
        # Basic validation for text fields
        if not data['sex'].lower() in ['male', 'female']:
            return False, "Sex must be 'male' or 'female'."
        
        if not data['hereditary_diseases']:
            return False, "Hereditary diseases cannot be empty."
        
        if not data['city']:
            return False, "City cannot be empty."
        
        if not data['job_title']:
            return False, "Job title cannot be empty."
        
        return True, "Valid input"
    except ValueError:
        return False, "Invalid input format. Ensure numeric fields contain valid numbers."

def calculate_prediction(data):
    """Simulate a prediction based on input data."""
    base_amount = 5000  # Base claim amount
    risk_score = 0
    
    # Age impact
    if data['age'] > 60:
        risk_score += 2000
    elif data['age'] > 40:
        risk_score += 1000
    
    # Health factors
    if data['smoker'] == 1:
        risk_score += 5000
    if data['diabetes'] == 1:
        risk_score += 3000
    if data['bmi'] > 30:
        risk_score += 2000
    if data['bloodpressure'] > 140:
        risk_score += 1500
    if data['regular_ex'] == 0:
        risk_score += 1000
    
    # Dependents and hereditary diseases
    risk_score += data['no_of_dependents'] * 500
    if data['hereditary_diseases'].lower() != 'none':
        risk_score += 2500
    
    # Final prediction
    total_amount = base_amount + risk_score
    return round(total_amount, 2)

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        input_data = {
            'age': request.form['age'],
            'sex': request.form['sex'],
            'weight': request.form['weight'],
            'bmi': request.form['bmi'],
            'hereditary_diseases': request.form['hereditary_diseases'],
            'no_of_dependents': request.form['no_of_dependents'],
            'smoker': request.form['smoker'],
            'city': request.form['city'],
            'bloodpressure': request.form['bloodpressure'],
            'diabetes': request.form['diabetes'],
            'regular_ex': request.form['regular_ex'],
            'job_title': request.form['job_title']
        }

        # Validate input
        is_valid, message = validate_input(input_data)
        if not is_valid:
            return render_template('index.html', prediction_text=f'Error: {message}')

        # Calculate prediction
        predicted_amount = calculate_prediction(input_data)

        # Return result to template
        return render_template('index.html', prediction_text=f'Estimated Claim Amount: ${predicted_amount}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        # Get JSON data
        input_data = request.get_json()
        if not input_data:
            return jsonify({'error': 'No input data provided'}), 400

        # Validate input
        is_valid, message = validate_input(input_data)
        if not is_valid:
            return jsonify({'error': message}), 400

        # Calculate prediction
        predicted_amount = calculate_prediction(input_data)

        return jsonify({
            'status': 'success',
            'predicted_amount': predicted_amount,
            'message': f'Estimated Claim Amount: ${predicted_amount}'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)