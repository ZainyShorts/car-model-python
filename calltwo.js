const { PythonShell } = require('python-shell');

async function loadModelAndPredict() {
    // Configure options for PythonShell
    const options = {
        pythonOptions: ['-u'], // unbuffered output
    };

    // Execute Python code
    PythonShell.runString(`
import pickle
import pandas as pd
from sklearn import preprocessing

# Load the model
with open('/Users/macbookpro/Documents/Python/Model/Husnain/Linear Regression/model_car.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to perform prediction
def price_predict(ec, myear, mile, company, varient, etype, trans, btype):
    cin = pd.DataFrame({
        'Engine Capacity': [ec],
        'Model Year': [myear],
        'Mileage': [mile],
        'Company': [company],
        'Vaarient': [varient],
        'Engine Type': [etype],
        'Transmission': [trans],
        'Body Type': [btype]
    })
    label_encoder = preprocessing.LabelEncoder()
    encoded_company = label_encoder.fit_transform(cin.Company)
    encoded_varient = label_encoder.fit_transform(cin.Vaarient)
    encoded_company = pd.Series(encoded_company)
    encoded_varient = pd.Series(encoded_varient)
    cin['Company'] = encoded_company
    cin['Vaarient'] = encoded_varient
    cout = model.predict(cin)
    return cout.tolist()[0]

# Perform prediction
prediction = price_predict(1000, 2005, 1536643, 'Suzuki', 'Cultus', 1, 1, 2)


`, options, (err, result) => {
        if (err) {
            console.error('PythonShell error:', err);
        } else {
            console.log('Prediction:', result);
        }
    });
}

async function main() {
    await loadModelAndPredict();
}

main().catch(console.error);
