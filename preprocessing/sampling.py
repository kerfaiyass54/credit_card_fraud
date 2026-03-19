from load_data.load_data import load_data
import pandas as pd



def sampling_data():
    data = load_data()

    legit = data[data.Class == 0]
    fraud = data[data.Class == 1]
    print("Legit class data: \n")
    print(legit.shape)

    print("Fraud class data: \n")
    print(fraud.shape)

    n_rows = min([legit.shape[0],fraud.shape[0]])

    sample_data = legit.sample(n=n_rows)

    sampled_dataset = pd.concat([sample_data, fraud], axis=0)

    return sampled_dataset


