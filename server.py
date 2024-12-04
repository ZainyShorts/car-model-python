import json
from flask import Flask, request , jsonify
from sklearn import preprocessing
import pickle
import pandas as pd
import numpy as np
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
CORS(app, origins='*')

with open('/Users/macbookpro/Documents/Python/Model/Husnain/Linear Regression/model_car.pkl', 'rb') as f:
    model = pickle.load(f)

def price_predict(ec,myear,mile,company,varient,etype,trans,btype):
  cin=pd.DataFrame({'Engine Capacity':[ec],
                   'Model Year':[myear],
                   'Mileage':[mile],
                   'Company':[company],
                    'Vaarient':[varient],
                   'Engine Type':[etype],
                   'Transmission':[trans],
                   'Body Type':[btype]})
  label_encoder = preprocessing.LabelEncoder()
  encoded_company = label_encoder.fit_transform(cin.Company)
  encoded_varient = label_encoder.fit_transform(cin.Vaarient)
  encoded_company = pd.Series(encoded_company)
  encoded_varient = pd.Series(encoded_varient)
  cin['Company'] = encoded_company
  cin['Vaarient'] = encoded_varient
  cout=model.predict(cin)
  cout = cout.tolist()
    
  result_df = pd.DataFrame({'prediction': cout})
  json_result = result_df.to_json(orient='records')
  parsed_json = json.loads(json_result )

  prediction = parsed_json[0]['prediction']
    
  return prediction



@app.route('/inspect/carmodel', methods=['POST'])
def imageValidater():
    print('test')
    data = request.json
    param1 = data.get('engineCapacity')
    param2 = data.get('modelYear')
    param3 = data.get('mileage')
    param4 = data.get('company')
    param5 = data.get('variant')
    param6 = data.get('engineType')
    param7 = data.get('transmission')
    param8 = data.get('bodyType')
    return jsonify({'price':price_predict(param1,param2,param3,param4,param5,param6,param7,param8)})

@app.route('/test', methods=['GET'])
def tester():
    print('test')
    return jsonify({'price':200})




if __name__ == '__main__':
    app.run(debug=True, port=8000) 
