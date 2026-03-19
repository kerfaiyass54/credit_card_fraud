from config.config import load_config
import pandas as pd

config = load_config()

raw_path     = config["dataset"]["location"]
cleaned_path = config["dataset"]["cleaned"]  
test_size    = config["model"]["test_size"]  
random_state = config["model"]["random_state"] 
target_class = config["target"]["name"]

def load_data():
    return pd.read_csv(raw_path)

def load_cleaned_data():
    return pd.read_csv(cleaned_path)

def load_class():
    return str(target_class)

def test_size_load():
    return int(test_size)

def random_state_load():
    return int(random_state)



