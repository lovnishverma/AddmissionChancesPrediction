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
    gre = eval(request.form.get("gre"))
    toefl = eval(request.form.get("toefl"))
    ur= eval(request.form.get("ur"))
    cgpa = eval(request.form.get("cgpa"))
    research = eval(request.form.get("research"))

    url = "predict_admission.csv"
    df = pd.read_csv(url)
    X = df.drop(['coa'], axis='columns')
    Y = df["coa"]
 
    model = LinearRegression()
    model.fit(X, Y)

  
    arr = model.predict([[gre,toefl, ur, cgpa,research]])

   
    return render_template("predict.html", data=arr[0])

if __name__ == '__main__':
    app.run()