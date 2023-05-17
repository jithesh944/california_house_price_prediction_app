import pickle
from flask import Flask,jsonify,render_template,url_for,request,app
import numpy as np
import pandas as pd


app = Flask(__name__)

lr_model = pickle.load(open('california_house_lr_model.pkl','rb'))
std_scalar = pickle.load(open('scalar_func.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    in_value_array = (np.array(list(data.values())).reshape(1,-1))
    print(in_value_array)
    transformed_in_value_array = std_scalar.transform(in_value_array)
    final_predict= lr_model.predict(transformed_in_value_array)
    print('final_predict',final_predict)
    return "Success"


if __name__ == '__main__':
    app.run(debug=True)




