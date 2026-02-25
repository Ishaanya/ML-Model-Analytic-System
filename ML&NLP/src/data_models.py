from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier

def regression_models():
    return {
        "Linear Regression" : LinearRegression(),
        "Ridge" : Ridge(), 
        "Lasso" : Lasso(), 
        "Random Forest Regressor" : RandomForestRegressor(random_state = 42)
    }

def classification_models():
    return {
        "Logistic Regression" : LogisticRegression(max_iter = 1000), 
        "Decision Tree Classifier" : DecisionTreeClassifier(), 
        "Random Forest Classifier" : RandomForestClassifier(), 
        "KNN" : KNeighborsClassifier() 
    }        

models = regression_models()
print(models)    