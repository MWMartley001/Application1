from flask import Flask
from google.cloud import automl_v1beta1 as automl
app = Flask(__name__)
app.config["DEBUG"] = True

def get_prediction(con_mo, con_one_year, con_two_year, deps, gend, net, mlines, pbilling, partner, phone_serv, sen_cit, ten, total_charge):
    # AutoML requirements
    project_id = 'application1-274321'
    compute_region = 'us-central1'
    model_display_name = 'telco_churn'
    inputs2 = {"contract_monthly": con_mo, "contract_one_year": con_one_year, "contract_two_year": con_two_year,
    "Dependents": deps, "gender": gend, "InternetService": net, "MultipleLines": mlines,
    "PaperlessBilling": pbilling, "Partner": partner, "PhoneService": phone_serv, "SeniorCitizen": sen_cit,
    "tenure": ten, "TotalCharges": total_charge}
    client = automl.TablesClient(project=project_id, region=compute_region)
    response = client.predict(model_display_name=model_display_name, inputs=inputs2)
    # return churn probability
    for result in response.payload[1:]:
        return("Predicted probability of churn: {}".format(result.tables.score))
