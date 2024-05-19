# Import the libraries
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


def make_predictions(data, model_vectorizer, model_predict):
    model_vec_load = joblib.load(model_vectorizer)
    model_pred_load = joblib.load(model_predict)
    new_data = pd.Series(data)
    new_data = preprocess.preprocess(new_data)

    model_trans = model_vec_load.transform(new_data)
    predict = model_pred_load.predict(model_trans)

    return int(predict)


if __name__ == '__main__':
    model_vec = r"..\Model\countvecterize.pkl"
    model_pred = r"..\Model\ann.pkl"
    predict = make_predictions("anh quý đang tuyển nhân viên cà phê đi bán cần",model_vec,model_pred)
    print(predict)