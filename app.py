import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from flask import Flask,request,jsonify,render_template

application=Flask(__name__)
app=application


ridge_model=pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler=pickle.load(open('models/scaler.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictheartdisease', methods=['Get', 'Post'])
def predict_heart_disease():

    if request.method=='POST':

        try:
            name = request.form.get('name')
            # age = int(request.form.get('age'))
            sex = request.form.get('sex')
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))
            general_health =  request.form.get('generalhealth')
            smoker_status = request.form.get('smokerstatus')
            alcohol_drinker = request.form.get('alcoholdrinker')
            diabetes = request.form.get('diabetes')
            stroke = request.form.get('stroke')
            kidney_disease = request.form.get('kidneydisease')
            asthma = request.form.get('asthma')
            cancer = request.form.get('cancer')
            phyactive = request.form.get('phyactive')
            difficulty_walking = request.form.get('diffwalking')
            sleeping_hours = float(request.form.get('sleephours'))

        except Exception as err:
            return render_template('index.html', result=err)

        # new_data_sc=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        # result=ridge_model.predict(new_data_sc)
        # return render_template('index.html', result=result[0])]

        msg_name = f"Hi {name},"
        message = f"The probability that you'll have heart disease is 2.03%. You are healthy!"

        return render_template('index.html', name=msg_name, message=message, img="https://c.tenor.com/MzMjocR0eIEAAAAd/tenor.gif")
        # https://clipart-library.com/2023/sick-heart-pain.gif
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)