from load_data.load_data import load_data
import pandas as pd


def clean_data(data):
    data.dropna()
    data.drop_duplicates(inplace=True)
    return data