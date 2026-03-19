from load_data.load_data import load_cleaned_data
from sklearn.model_selection import train_test_split
from load_data.load_data import load_class
from load_data.load_data import test_size_load
from load_data.load_data import random_state_load



df = load_cleaned_data()

target_name = load_class()

X = df.drop(columns=target_name, axis=1)
Y = df[target_name]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size_load(), stratify=Y, random_state=random_state_load())

def get_x_train():
    return X_train

def get_y_train():
    return Y_train

def get_x_test():
    return X_test

def get_y_test():
    return Y_test
