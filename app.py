from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')


@app.route('/')
def home():
    return "flask is working"


@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
