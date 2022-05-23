import pickle
import numpy as np
import flask
from sklearn.preprocessing import Normalizer
from flask import Flask
from flask import request, url_for, redirect, render_template
import sys
sys.setrecursionlimit(10000)

app = Flask(__name__)

model = pickle.load(open("pickle_colab.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/colab", methods=["POST", "GET"])
def temp():
    features_encode = []
    prediction = None
    if flask.request.method == 'POST':
        input_val = [i for i in request.form.values()]
        # uncat = input_val[0:48]
        # Normalized = Normalizer().fit_transform(np.array(input_val).reshape(-1, 1))
        # features = [j for j in input_val[0:48]]
        for z in input_val:
            if z == "Ya":
                features_encode.append(1)
            elif z == "Tidak":
                features_encode.append(0)

        # for k in Normalized:
        #     features_encode.append(int(k))
        prediction = model.predict(np.array(features_encode).reshape(1, -1))
        if int(prediction) == 0:
            prediction = "Akademik dan Kebahasaan"
        elif int(prediction) == 1:
            prediction = "Bela Negara"
        elif int(prediction) == 2:
            prediction = "IT"
        elif int(prediction) == 3:
            prediction = "Kesenian"
        elif int(prediction) == 4:
            prediction = "Lingkungan Hidup"
        elif int(prediction) == 5:
            prediction = "Olahraga"

    return render_template("form.html", features_encode=features_encode, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
