import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data
from sklearn.preprocessing import StandardScaler # used for feature scaling


app = Flask(__name__)
model = pickle.load(open('C:/Users/Ashmita Agrawal/Desktop/Learning/Deployment of project using Flask/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        #final_features = np.array([37,'30 to 49',4,'Home Care',122,0,'Medical',1,1,5511.95,5582.49,1.0128])
        labelencoder_X = LabelEncoder()
        final_features = request.form
        for i in final_features:
            final_features= labelencoder_X.fit_transform(final_features)
        
        final_features = np.array([final_features])
        prediction = model.predict(final_features)
        output = prediction[0]
        if output == 1:
           output = "Genuine"
        else:
            output == "Fraud"
        print(output)

    return render_template("index.html",prediction_text = "The case is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)