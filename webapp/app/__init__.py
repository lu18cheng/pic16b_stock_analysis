# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import tensorflow as tf
from tensorflow import keras

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# from tensorflow.keras.layers import Input, Dense, Activation,Dropout
# from tensorflow.keras.models import Model
# from tensorflow.keras import layers
# from tensorflow.keras import layers
# from tensorflow.keras import losses



import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


import io
import base64


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)

@app.route('/')

# def main():
#     return render_template("main.html")

# comment out the below to focus on just the fundamentals

# after running
# $ export FLASK_ENV=development; flask run
# site will be available at 
# http://localhost:5000

def main():
    return render_template('main_better.html')

# Show url matching

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/hello/<name>/')
def hello_name(name):
    return render_template('hello.html', name=name)

# Page with form

@app.route('/ask/', methods=['POST', 'GET'])
def ask():
    if request.method == 'GET':
        return render_template('ask.html')
    else:
        try:
            return render_template('ask.html', name=request.form['name'], student=request.form['student'])
        except:
            return render_template('ask.html')

# File uploads and interfacing with complex Python
# basic version

@app.route('/submit-basic/', methods=['POST', 'GET'])
def submit_basic():
    if request.method == 'GET':
        return render_template('submit-basic.html')
    else:
        try:
            return render_template('submit-basic.html', thanks = True)
        except:
            return render_template('submit-basic.html', error=True)

@app.route('/submit-advanced/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            # retrieve the necessary data
            type = request.form['type']
            treasury = request.form['treasury']
            inflation = request.form['inflation']
            CPI = request.form['CPI']
            exchange = request.form['exchange']

            # prepare for prediction
            test_data =  tf.data.Dataset.from_tensor_slices(
                (
                    {
                        "Treasury10yr_PercentChange": np.array([treasury]).reshape(-1,1),
                        "inflation5yr_PercentChange": np.array([inflation]).reshape(-1,1),
                        "CPI_PercentChange"         : np.array([CPI]).reshape(-1,1),
                        "exchange_PercentChange"    : np.array([exchange]).reshape(-1,1)
                    }
                )
            )

            # model prediction
            if type == "value":
                model = pickle.load(open("../model/mixed_regression_value.pkl",'rb'))
                result = model.predict(test_data)[0][0]
            else:
                model = pickle.load(open("../model/mixed_regression_growth.pkl",'rb'))
                result = model.predict(test_data)[0][0]

            return render_template('submit.html', result=result)
        except:
            return render_template('submit.html', error=True)