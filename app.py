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
    GRE_score = eval(request.form.get("GRE_score"))
    TOEFL = eval(request.form.get("TOEFL"))
    University_rating= eval(request.form.get("University_rating"))
    CGPA = eval(request.form.get("CGPA"))
    Research = eval(request.form.get("Research"))
    Chance_of_admit = eval(request.form.get(""))

    url = "cbp.csv"
    df = pd.read_csv(url)
    X = df.drop(['ID', 'Calories'], axis='columns')
    Y = df["Calories"]

 
    model = LinearRegression()
    model.fit(X, Y)

  
    arr = model.predict([[GRE_score,TOEFL, University_rating, CGPA,Research]])

   
    return render_template("calorie.html", data=arr[0])

if _name_ == '_main_':
    app.run()