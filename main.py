#front-end file

from flask import Flask, request
from google.cloud import automl_v1beta1 as automl
from predictor import get_prediction
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        con_mo = None
        con_one_year = None 
        con_two_year = None 
        deps = None 
        gend = None 
        net = None 
        mlines = None
        pbilling = None 
        partner = None 
        phone_serv = None 
        sen_cit = None 
        ten = None 
        total_charge = None 
        try: 
            con_mo = str(request.form["Monthly_Contract"])
            con_one_year = str(request.form["Annual_Contract"])
            con_two_year = str(request.form["Two_Year_Contract"])
            deps = str(request.form["Dependents"])
            gend = str(request.form["Gender"])
            net = str(request.form["Internet"])
            mlines = str(request.form["Multiple_Lines"])
            pbilling = str(request.form["Paperless_Billing"])
            partner = str(request.form["Partner"])
            phone_serv = str(request.form["Phone_Service"])
            sen_cit = str(request.form["Senior_Citizen"])
            ten = int(request.form["Tenure"])
            total_charge = float(request.form["Total_Charges"])
        except:
            errors += "<p>Something is wrong.</p>\n"
        result = get_prediction(con_mo,con_one_year,con_two_year,deps,gend,net,mlines,pbilling,partner,phone_serv,sen_cit,ten,total_charge)
        return '''
            <html>
                <body>
                    <p>{result}</p>
                    <p><a href="/">Click here to calculate again</a>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <h1>Churn Probability Estimator: Telco</h1>
                <p>Enter the inputs:</p>
                <form method="post" action=".">
                    <p>Monthly Contract? <input name="Monthly_Contract" /></p>
                    <p>Annual Contract? <input name="Annual_Contract" /></p>
                    <p>Two Year Contract? <input name="Two_Year_Contract" /></p>
                    <p>Dependents? <input name="Dependents" /></p>
                    <p>Gender? <input name="Gender" /></p>
                    <p>Internet? <input name="Internet" /></p>
                    <p>Multiple Lines? <input name="Multiple_Lines" /></p>
                    <p>Paperless Billing? <input name="Paperless_Billing" /></p>
                    <p>Partner? <input name="Partner" /></p>
                    <p>Phone Service? <input name="Phone_Service" /></p>
                    <p>Senior Citizen? <input name="Senior_Citizen" /></p>
                    <p>Tenure? <input name="Tenure" /></p>
                    <p>Total Charges? <input name="Total_Charges" /></p>
                    <p><input type="submit" value="Get Prediction" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)


if __name__ == '__main__': 
    app.run()
