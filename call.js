const { Python } = require('pyodide');

// Load and initialize Python
async function loadPython() {
    await Python.load();
}

// Execute Python code to load and deserialize the model
async function loadModelAndPredict() {
    const pythonCode = `
import json
from sklearn import preprocessing
import pickle
import pandas as pd
import numpy as np

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
    
    # Convert the prediction result to a DataFrame
  result_df = pd.DataFrame({'prediction': cout})
    
    # Serialize the DataFrame to JSON
  json_result = result_df.to_json(orient='records')
  parsed_json = json.loads(json_result )

  prediction = parsed_json[0]['prediction']
    
  return prediction

  price_predict(1000,2005,1536643,'Suzuki','Cultus',1,1,2)

`;

    const result = await Python.run(pythonCode);
    console.log('Prediction:', result);
}

// Load Python and perform prediction
async function main() {
    await loadPython();
    await loadModelAndPredict();
}

main().catch(console.error);
