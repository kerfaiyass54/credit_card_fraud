from preprocessing.preprocess import preprocess_data
from train.train_model import train_model
import uvicorn

if __name__ == "__main__":
    preprocess_data()
    train_model()
    uvicorn.run("api.api:app", host="0.0.0.0", port=8000, reload=False)