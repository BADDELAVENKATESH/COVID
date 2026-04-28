from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    confirmed = float(request.form['confirmed'])
    deaths = float(request.form['deaths'])

    prediction = model.predict([[confirmed, deaths]])[0]

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)