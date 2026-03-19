from config.config import load_config
import pandas as pd

config = load_config()

raw_path     = config["dataset"]["location"]
cleaned_path = config["dataset"]["cleaned"]  
test_size    = config["model"]["test_size"]  
random_state = config["model"]["random_state"] 

def load_data():
    return pd.read_csv(raw_path)



