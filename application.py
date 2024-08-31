from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
# model_names,description,manufacturer,modelDate,engineDisplacement,price,mileageFromOdometer,vehicleTransmission,fuelType,
app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('RandomForestModel.pkl','rb'))
car=pd.read_csv('model_data.csv')
company_models = {}

@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car['manufacturer'].unique())
    car_models = sorted(map(str, car['model_names'].unique()))
    year=sorted(car['modelDate'].unique(),reverse=True)
    fuel_type=car['fuelType'].unique()
    # print(companies,car_models,year,fuel_type)

    
    for company in companies:
        company_models[company] = sorted(map(str, car[car['manufacturer'] == company]['model_names'].unique()))

    company_models['Select Company'] = []  # Add a default entry


    print(f"this is a dic: \n {company_models} \n\n this a car models: \n\n{car_models} this is companies:\n\n{companies}")
    
    return render_template('index.html', 
                           companies=companies, 
                           car_models=car_models, 
                           years=year, 
                           fuel_types=fuel_type, 
                           company_models=company_models)


@app.route('/your-endpoint', methods=['POST'])
def your_function():
    company = request.json.get('company')
    models = company_models.get(company, [])
    return jsonify(models=models)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    company=request.form.get('company')

    car_model=request.form.get('car_models')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kilo_driven')

    prediction=model.predict(pd.DataFrame(columns=['model_names', 'manufacturer', 'modelDate', 'mileageFromOdometer', 'fuelType'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    print(prediction)

    return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run()
