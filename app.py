from flask import Flask,request,render_template
import numpy as np
import pandas as pd
#import pandas
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
import pickle

# Importar los modelos
encoder = pickle.load(open('encoder.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
transformers = pickle.load(open('transformers.pkl','rb'))
model_pipe = pickle.load(open('model_pipe.pkl','rb'))

# crear flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    sl_no = request.form['sl_no']
    gender = request.form['gender']
    ssc_p = request.form['ssc_p']
    hsc_p = request.form['hsc_p']
    degree_p = request.form['degree_p']
    workex = request.form['workex']
    etest_p = request.form['etest_p']
    specialisation = request.form['specialisation']
    mba_p = request.form['mba_p']

    sample = pd.DataFrame({'sl_no': [sl_no],
                           'gender': [gender],
                           'ssc_p': [ssc_p],
                           'hsc_p': [hsc_p],
                           'degree_p': [degree_p],
                           'workex': [workex],
                           'etest_p': [etest_p],
                           'specialisation': [specialisation],
                           'mba_p': [mba_p]})
    
    prediction = model_pipe.predict(sample)[0]

    diccionario = {0: 'contratado', 1: 'no contratado'}

    if prediction in diccionario:
        crop = diccionario[prediction]
        result =("{}".format(crop))
    else:
        result =("Sorry, tas tilin")
    return render_template('index.html',result = result)




# python main
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)