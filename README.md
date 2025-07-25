# Claim Amount Prediction

A web application and machine learning pipeline for predicting insurance claim amounts based on user-provided health, demographic, and lifestyle information.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project aims to estimate health insurance claim amounts by leveraging user data such as age, gender, BMI, smoking status, hereditary diseases, and other factors. It combines a Python Flask web interface with machine learning models developed using Jupyter Notebooks and PyCaret.

Users can enter their details through a form, and the app will predict the expected claim amount using advanced regression models and custom heuristics.

---

## Features

- **Web Interface**: User-friendly web form for input and instant prediction results.
- **REST API**: `/api/predict` endpoint for programmatic access.
- **Advanced Modeling Pipeline**: Data preprocessing, feature engineering, cross-validation, and ensemble predictions (see Jupyter Notebook).
- **Visualization Dashboard**: (Optional) Dashboard for policy overview and claim history.
- **Extensible**: Easily swap models and extend features.

---

## Tech Stack

- Python (Flask, Pandas, PyCaret)
- Jupyter Notebook
- HTML/CSS (TailwindCSS, FontAwesome)
- (Optional) Streamlit for interactive notebook UI

---

## Setup & Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/Manshachaudhary/claim-amount-prediction.git
   cd claim-amount-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Model**
   - Make sure `insurance_claim_model` (PyCaret model) is available in the project root.
   - For advanced notebook workflows, see `prepros-checkpoint.ipynb`.

5. **Run the App**
   ```bash
   python app.py
   ```
   Access it at [http://localhost:5000](http://localhost:5000)

---

## Usage

### Web Interface

- Visit the home page.
- Fill in details such as age, sex, BMI, smoker status, etc.
- Submit the form to see the predicted claim amount.

### REST API

- Make a POST request to `/api/predict` with JSON body:
  ```json
  {
    "age": 45,
    "sex": "male",
    "weight": 75,
    "bmi": 27.5,
    "hereditary_diseases": "diabetes",
    "no_of_dependents": 2,
    "smoker": 1,
    "city": "Delhi",
    "bloodpressure": 130,
    "diabetes": 1,
    "regular_ex": 0,
    "job_title": "Engineer"
  }
  ```
- Response:
  ```json
  {
    "status": "success",
    "predicted_amount": 14500,
    "message": "Estimated Claim Amount: $14500"
  }
  ```

---

## Model Details

- **Preprocessing**: Outlier handling, feature scaling (RobustScaler), label encoding for categorical variables.
- **Feature Engineering**: Interactions (e.g., age × BMI), health/risk indices.
- **Modeling**: Regression models via PyCaret, ensemble and uncertainty estimates.
- **Evaluation**: Metrics like R², cross-validation scores (see notebook for details).

---

## Project Structure

```
claim-amount-prediction/
│
├── app.py                    # Flask web app
├── app_t.py                  # API and extended logic
├── requirements.txt
├── insurance_claim_model      # Trained PyCaret model
├── templates/
│   ├── index.html            # Web UI
│   └── dashboard.html        # (Optional) Dashboard
├── prepros-checkpoint.ipynb  # Jupyter notebook for advanced ML
└── README.md                 # This file
```

---

## Contributing

Contributions are welcome! Please fork the repo and submit a pull request, or open an issue for suggestions and bugs.

---

## License

This project currently does **not** specify a license. Please contact the owner for details.
