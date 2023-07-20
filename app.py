from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/r')
def predict():
    return render_template('predict.html')

@app.route('/cp', methods=['POST'])
def predict_admission():
    GRE_score = eval(request.form.get("GRE_score"))
    TOEFL = eval(request.form.get("TOEFL"))
    University_rating= eval(request.form.get("University_rating"))
    CGPA = eval(request.form.get("CGPA"))
    Research = eval(request.form.get("Research"))
    Chance_of_admit = eval(request.form.get("Chance_of_admit"))

    url = "predict_admission.csv"
    df = pd.read_csv(url)
    X = df.drop(['Chance_of_admit'], axis='columns')
    Y = df["Chance_of_admit"]

 
    model = LinearRegression()
    model.fit(X, Y)

  
    arr = model.predict([[GRE_score,TOEFL, University_rating, CGPA,Research,Chance_of_admit]])

   
    return render_template("predict.html", data=arr[0])

if __name__ == '__main__':
    app.run()