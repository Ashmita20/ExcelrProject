import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.preprocessing import StandardScaler # used for feature scaling


app = Flask(__name__,template_folder='templates')
app.secret_key = 'G1123'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
        Days_spend_hsptl = request.form.get('Days_Spend_in_Hospital')  
        ccs_diagnosis_code = request.form.get('CCS_diagnosis_code')
        ccs_procedure_code = request.form.get('CCS_procedure_code')  
        Hospital_id = request.form.get('Hospital_Id')
        Tot_charg = request.form.get('Total_Charge')
        Tot_cost = request.form.get('Total_Cost')  
        ratio = request.form.get('Ratio_of_total_cost_charge')
        Surge_Description = request.form.get('Surge_Description') 
        Age = request.form.get('Age')
        Home_Care_Self_Care = request.form.get('Home_Care_Self_Care')
        Mortality_Risk = request.form.get('Mortality_Risk')  
        Code_Illness = request.form.get('Code_Illness')
        final_features=["Hospital_id","Age","Days_spend_hsptl","Home_Care_Self_Care",
                             "ccs_diagnosis_code","ccs_procedure_code","Surge_Description","Code_Illness",
                             "Mortality_Risk","Tot_charg","Tot_cost","ratio"]
        labelencoder_X = LabelEncoder()
        for i in final_features:
            final_features= labelencoder_X.fit_transform(final_features)
        
        final_features = np.array([final_features])
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(final_features)
        output = prediction[0]
        if output == 1:
            output = "Insurance Claim is Genuine"
        else:
             output == "Insurance Claim is Fraud"
        print(output)
        return(render_template('index.html',prediction_text='{}'
                                     .format(output )))
            
#             
# =============================================================================
#     if request.method == 'POST':
#         model = pickle.load(open('model.pkl', 'rb'))
#         #final_features = np.array([37,'30 to 49',4,'Home Care',122,0,'Medical',1,1,5511.95,5582.49,1.0128])
#         labelencoder_X = LabelEncoder()
#         final_features = [x for x in request.form.get()]
#         for i in final_features:
#             final_features= labelencoder_X.fit_transform(final_features)
#         
#         final_features = np.array([final_features])
#         prediction = model.predict(final_features)
#         output = prediction[0]
#         if output == 1:
#            output = "Genuine"
#         else:
#             output == "Fraud"
#         print(output)
# 
# =============================================================================
    #return redirect(url_for("after"))

    
@app.route('/after')  
def after():
    return(render_template('after.html'))
if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
