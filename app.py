from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/page')
def page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    gre = eval(request.form.get("gre"))
    toefl = eval(request.form.get("toefl"))
    ur = eval(request.form.get("ur"))
    cgpa = eval(request.form.get("cgpa"))
    research = eval(request.form.get("research"))

    # Load the dataset
    url="admission.csv"
    df=pd.read_csv(url, header=None)
    # Prepare the data
    X=df[:,:5]
    y=df[:,-1]

    # Create a random forest classifier model
    model = LinearRegression()

    # Train the model on the entire dataset
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gre, toefl, ur, cgpa, research]]
    prediction = int(model.predict(new_data)[0])

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)