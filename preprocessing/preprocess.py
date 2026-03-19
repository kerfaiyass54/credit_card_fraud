from preprocessing.cleaning_data import clean_data
from preprocessing.sampling import sampling_data
from config.config import load_config
import pandas as pd

def preprocess_data():
    df = sampling_data()
    df = clean_data(df)
    config = load_config()
    pd.DataFrame.to_csv(config["dataset"]["cleaned"])
