from flask import Flask , render_template , request
import dill as pickle
import pandas as pd , numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib , scipy.sparse , re

app = Flask(__name__)

port_stemmer= PorterStemmer()
reuters_removal = pickle.load(open("models/reuters_removal.pkl" , "rb"))
stemmer = pickle.load(open("models/stemmer.pkl", "rb"))
model = joblib.load("models/news_detector.joblib")
rfc_model = model['rfc_model']
gbm_model = model['gbm']
lgr_model = model['lgr']
vectorization = model['vectorizer']
manual_tester = pickle.load(open("models/manual_tester.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict" , methods = ['POST' , 'GET']) 
def predict():
    sample = request.form.get("text")
    pred = -1
    pred = manual_tester(sample)
    print(pred)
    pred1 = -1
    pred2 = -1
    pred3 = -1
    return render_template("index.html" , pred1 = pred[0] , pred2 = pred[1] , pred3 = pred[2] , pred =  pred)


if __name__ == "__main__":
    print("Running Fake News Detector flask server")
    app.run(debug = True)
