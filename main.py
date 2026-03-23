from preprocessing.preprocess import preprocess_data
from train.train_model import train_model

if __name__ == "__main__":
    preprocess_data()
    train_model()