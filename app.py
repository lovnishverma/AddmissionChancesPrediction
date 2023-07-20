from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/r')
def predict():
    return render_template('calorie.html')

@app.route('/cp', methods=['POST'])
def caloriesburntpredict():
    Age = eval(request.form.get("Age"))
    Duration = eval(request.form.get("Duration"))
    Heart_Rate = eval(request.form.get("Heart_Rate"))
    Body_Temp = eval(request.form.get("Body_Temp"))


    url = "cbp.csv"
    df = pd.read_csv(url)
    X = df.drop(['ID', 'Calories'], axis='columns')
    Y = df["Calories"]

 
    model = LinearRegression()
    model.fit(X, Y)

  
    arr = model.predict([[Age, Duration, Heart_Rate, Body_Temp]])

   
    return render_template("calorie.html", data=arr[0])

if _name_ == '_main_':
    app.run()