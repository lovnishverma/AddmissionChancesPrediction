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
    gre = int(request.form.get("gre"))
    toefl = int(request.form.get("toefl"))
    ur = int(request.form.get("ur"))
    cgpa = float(request.form.get("cgpa"))
    research = int(request.form.get("research"))

    # Load the dataset
    url = "admission.csv"
    df = pd.read_csv(url, header=None)

    # Prepare the data
    X = df.iloc[:, :5]
    y = df.iloc[:, -1]

    # Create a linear regression model
    model = LinearRegression()

    # Train the model on the entire dataset
    model.fit(X, y)

    # Make prediction on new data
    new_data = [[gre, toefl, ur, cgpa, research]]
    prediction = model.predict(new_data)[0]

    # Convert the prediction to percentage format
    prediction_percentage = prediction * 100

    return render_template('predict.html', prediction=prediction_percentage)

if __name__ == '__main__':
    app.run(debug=True)