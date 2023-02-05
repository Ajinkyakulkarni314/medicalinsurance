from flask import Flask, render_template,jsonify,request
import config # As port Number and path are stored in this file 
from project_app.utils import MedicalInsurance


app  = Flask(__name__)

@app.route("/")  # Rule >> API name (/ >> Home API)
def hello():
    print("Welcome to flask")
    return render_template('home.html')

    ################################################################################################
@app.route('/predict_charges',methods=['POST'])
def get_insurance_charges():
    #data=request.form  # for postman data
    # age=67         # This hardcore data for browser based manual input
    # sex='male'     # Not Required in case of postman
    # bmi=28.3
    # children=3
    # smoker='yes'


    age=eval(request.form['age'])     # as postaman gives data in dictionary format we access it through dict_name['key]
    sex=request.form['sex']            # as value enteredin postman are returned all as string
    bmi=eval(request.form['bmi'])        # where ever int dat we use eval funct to chage datatype
    children=eval(request.form['children'])
    smoker=request.form['smoker']
    region=request.form['region']

    med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=med_ins.get_predicted_charges()
    return render_template("next.html",data=charges) 

######################################################################################
app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True) #server start

