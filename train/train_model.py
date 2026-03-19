from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from train.data_split import get_x_train, get_y_train, get_x_test, get_y_test
from load_data.load_data import load_model


def train_model():
    model = LogisticRegression()
    X_train = get_x_train()
    Y_train = get_y_train()
    X_test = get_x_test()
    Y_test = get_y_test()
    model_path = load_model()
    model.fit(X_train, Y_train)
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
    print('Accuracy score on Test Data : ', test_data_accuracy)
    joblib.dump(model, model_path)
    print(f'Model saved to {model_path}')
    return model