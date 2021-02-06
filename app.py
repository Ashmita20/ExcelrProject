import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:/Users/Ashmita Agrawal/Desktop/Learning/Deployment of project using Flask/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    
    #final_features = np.array([[1,1,1,1,1,1,1,1,1,1,1,1]])
    #prediction = model.predict(final_features)
    #print(prediction)
    int_features = request.form
    #prediction = request.form.get("Hospital_Id")
    final_features = np.array([[int_features]])
    prediction = model.predict(final_features)
# =============================================================================
#     if prediction == 1:
#        output = "Its not a fraud case"
#     else:
#         output = "Its a fraud"
# 
# =============================================================================
    output = prediction[0]

    return render_template('after.html')

if __name__ == "__main__":
    app.run(debug=True)