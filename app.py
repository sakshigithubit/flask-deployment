from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model-p.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')

    input_query = np.array([[cgpa,iq,profile_score]])
    input_query = input_query.astype(np.float64)
    result = model.predict(input_query)[0]

    return jsonify({'placement':str(result)})

