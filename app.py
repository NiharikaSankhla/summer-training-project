from flask import Flask, render_template, request
import pickle
import pandas as pd

print("TEST CHANGE 999")

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():

    prediction_text = ""
    survival_probability = ""

    if request.method == 'POST':

        Pclass = int(request.form['Pclass'])
        Sex = int(request.form['Sex'])
        Age = float(request.form['Age'])
        SibSp = int(request.form['SibSp'])
        Parch = int(request.form['Parch'])

        input_df = pd.DataFrame(
            [[Pclass, Sex, Age, SibSp, Parch]],
            columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
        )

        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)

        survival_probability = f"{probability[0][1] * 100:.2f}"

        if prediction[0] == 1:
            prediction_text = "Passenger Survived"
        else:
            prediction_text = "Passenger Did Not Survive"

    return render_template(
        'index.html',
        prediction_text=prediction_text,
        survival_probability=survival_probability,
        model_name="Logistic Regression"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)