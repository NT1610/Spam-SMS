import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
import preprocess 
import joblib

def make_predictions_vectorrizer(data, model_vectorizer, model_predict):
    model_vec_load = joblib.load(model_vectorizer)
    model_pred_load = joblib.load(model_predict)

    new_data = pd.Series(data)
    new_data = preprocess.preprocess(new_data)

    model_trans = model_vec_load.transform(new_data)
    predict = model_pred_load.predict(model_trans)
    predict = [int(i) for i in predict]
    return predict

if __name__ == '__main__':
    model_vec = r"..\Model\tfidf.pkl"
    model_pred = r"..\Model\logistic.pkl"
    model_vec_load = joblib.load(model_vec)
    model_pred_load = joblib.load(model_pred)
    predict = make_predictions_vectorrizer(["Công ty anh quý, tuyển người bán cần"],model_vec_load,model_pred_load)
    print(predict)
