from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():

    prediction_text = ""

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

        survival_probability = probability[0][1] * 100
        if prediction[0] == 1:
            prediction_text = "Passenger Survived"
        else:
            prediction_text = "Passenger Did Not Survive"

    return render_template(
        'index.html',
        prediction_text=prediction_text,
        survival_probability=f"{survival_probability:.2f}" if request.method == 'POST' else "",
        model_name="Logistic Regression"
    )
if __name__ == '__main__':
    app.run(debug=True)