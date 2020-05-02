from flask import Flask
from google.cloud import automl_v1beta1 as automl
app = Flask(__name__)

# AutoML requirements/inputs for prediction
project_id = 'application1-274321'
compute_region = 'us-central1'
model_display_name = 'telco_churn'
inputs = {"contract_monthly": '0', "contract_one_year": '0', "contract_two_year": '1',
 "Dependents": '1', "gender": '1', "InternetService": '1', "MultipleLines": '1',
 "PaperlessBilling": '1', "Partner": '0', "PhoneService": '1', "SeniorCitizen": '0',
 "tenure": 6, "TotalCharges": 300.00}

# homepage
@app.route('/')
def placeholder():
    return "Churn Predictions"

# return predictions
@app.route('/predict', methods=['GET', 'POST'])
def get_result():
    client = automl.TablesClient(project=project_id, region=compute_region)
    response = client.predict(model_display_name=model_display_name, inputs=inputs)
    print("Prediction results:")
    return str(response.payload)

if __name__ == '__main__': 
    app.run()
