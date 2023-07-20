from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import LogisticRegression

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

    # Load the loan dataset
    df = pd.read_csv('admission.csv')

    # Prepare the data
    X=df[:,:5]
    y=df[:,-1]

    # Create a random forest classifier model
    model = LogisticRegression()

    # Train the model on the entire dataset
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gre, toefl, ur, cgpa, research]]
    prediction = int(model.predict(new_data)[0])

    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)