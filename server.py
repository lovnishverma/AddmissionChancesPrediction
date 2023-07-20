from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    gre = eval(request.form.get("gre"))
    toefl = eval(request.form.get("toefl"))
    ur = eval(request.form.get("ur"))
    cgpa = eval(request.form.get("cgpa"))
    research = eval(request.form.get("research"))


    # Load the loan dataset
    df = pd.read_csv('predict_admission.csv')

    # Prepare the data
    X = df[['gre','toefl', 'ur', 'cgpa','research']]
    y = df['coa']

    # Create a random forest classifier model
    model = RandomForestClassifier()

    # Train the model on the entire dataset
    model.fit(X, y)

    # Make prediction on new data
    new_data = ([[gre,toefl, ur, cgpa,research]])
    prediction = int(model.predict(new_data)[0])

    return render_template('predict.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)