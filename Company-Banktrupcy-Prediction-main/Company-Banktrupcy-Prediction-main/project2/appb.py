from flask import Flask, render_template,request,jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app  = Flask(__name__)

#Load the pickle model
model=pickle.load(open('modelg.pkl','rb'))

@app.route('/')
def index():
    return render_template('indexs.html')


@app.route('/predict', methods=['GET','post'])
def predict():
    Operating_Gross_Margin = float(request.form['Operating Gross Margin'])
    Cash_flow_rate = float(request.form['Cash flow rate'])
    Tax_rate_A = float(request.form['Tax rate (A)'])
    Net_worth_Assets = float(request.form['Net worth/Assets'])
    Total_Asset_Turnover = float(request.form['Total Asset Turnover'])
    Cash_Total_Assets = float(request.form['Cash/Total Assets'])
    Cash_Current_Liability = float(request.form['Cash/Current Liability'])
    Total_income_Total_expense = float(request.form['Total income/Total expense'])
    Total_expense_Assets = float(request.form['Total expense/Assets'])
    Gross_Profit_to_Sales = float(request.form['Gross Profit to Sales'])
    
    predict = model.predict([[Operating_Gross_Margin,Cash_flow_rate,Tax_rate_A,Net_worth_Assets,Total_Asset_Turnover,Cash_Total_Assets,Cash_Current_Liability,Total_income_Total_expense,Total_expense_Assets,Gross_Profit_to_Sales]])
    
    output = predict[0]
    
    return render_template('indexs.html',result=output)
    
if __name__ == "__main__":
    app.run(debug=True)
    