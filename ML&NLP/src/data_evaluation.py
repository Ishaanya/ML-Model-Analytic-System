from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score 

import numpy as np 

def regression_metrics(y_true, y_pred):
    return {
        "MAE" : mean_absolute_error(y_true, y_pred),
        "RMSE" : np.sqrt(mean_squared_error(y_true, y_pred)), 
        "R2" : r2_score(y_true, y_pred)
    }

def classification_metrics(y_true, y_pred):
    return {
        "Accuracy" : accuracy_score(y_true, y_pred), 
        "Precision Score" : precision_score(y_true, y_pred, average = "weighted"), 
        "Recall" : recall_score(y_true, y_pred, average = "weighted"), 
        "F1" : f1_score(y_true, y_pred, average = "weighted") 
    }    