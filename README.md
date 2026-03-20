
# 🚨 Credit Card Fraud Detection Pipeline

[![My Skills](https://skillicons.dev/icons?i=py,docker,git,github,postman)](https://skillicons.dev)

---

## 🚀 **Overview**

**Detect fraudulent credit card transactions with a robust machine learning pipeline!**

This repository provides a **complete, production-ready credit card fraud detection system** built with Python. It includes:

✅ **Data preprocessing** (cleaning, sampling, and balancing)

✅ **Exploratory Data Analysis (EDA)** for insights

✅ **Train-test split** with stratification

✅ **Logistic Regression model** for fraud detection

✅ **Model persistence** (saving trained models)

✅ **Configurable pipeline** via YAML

Perfect for **data scientists, ML engineers, and fraud analysts** who want to build, test, and deploy fraud detection models quickly.

---

## ✨ **Features**

🔹 **End-to-end fraud detection pipeline** – From raw data to trained model

🔹 **Class imbalance handling** – Balances fraudulent vs. legitimate transactions

🔹 **Modular design** – Easy to extend with new models or preprocessing steps

🔹 **Configurable via YAML** – Adjust paths, test sizes, and model parameters

🔹 **Visualization tools** – Quick EDA with missing value and duplicate checks

🔹 **Model persistence** – Save trained models for deployment

---

## 🛠️ **Tech Stack**

| Category       | Tools/Libraries                          |
|----------------|------------------------------------------|
| **Language**   | Python 3.8+                              |
| **ML Frameworks** | Scikit-learn (`LogisticRegression`)     |
| **Data Handling** | Pandas, NumPy                          |
| **Configuration** | PyYAML                                  |
| **Model Persistence** | Joblib (`joblib.dump`)                |
| **Testing**    | Scikit-learn’s `train_test_split`       |

**System Requirements:**
- Python 3.8+
- Pandas ≥ 1.3.0
- Scikit-learn ≥ 1.0.0
- PyYAML ≥ 5.4.1
- Jupyter Notebook (optional, for visualization)

---

## 📦 **Installation**

### **Prerequisites**
Ensure you have Python 3.8+ installed. If not, download it from [python.org](https://www.python.org/downloads/).

### **Quick Start**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/credit_card_fraud.git
   cd credit_card_fraud
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` doesn’t exist, run `pip install pandas scikit-learn pyyaml joblib` manually.)*

4. **Download the dataset:**
   - The pipeline expects a `creditcard.csv` file in the `dataset/` directory.
   - You can download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) or use the provided script to fetch it automatically.



## 🔧 **Configuration**
### **Environment Variables**
No environment variables are required, but you can override paths dynamically:
```python
from config.config import load_config
config = load_config(config_path="custom_config.yml")  # Use a custom config
```

### **Customization Options**
- **Change the model:** Replace `LogisticRegression` in `train_model.py` with `RandomForestClassifier` or `XGBoost`.
- **Add more preprocessing:** Extend `preprocessing/cleaning_data.py` or `preprocessing/sampling.py`.
- **Deploy the model:** Use `joblib.load("models/model.pkl")` in a Flask/Django app.

---

## 🤝 **Contributing**
We welcome contributions! Here’s how you can help:

1. **Fork the repository** and clone it locally.
2. **Create a new branch** for your feature/bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Install dependencies** (as above) and run tests (if any).
4. **Commit your changes** with a clear message:
   ```bash
   git commit -m "Add support for XGBoost model"
   ```
5. **Push to your fork** and open a **Pull Request**!

### **Development Setup**
- Use `pre-commit` to enforce code style (if available).
- Run tests with `pytest` (if tests exist).
- Follow the [Python style guide (PEP 8)](https://peps.python.org/pep-0008/).

### **Code Style Guidelines**
- Use **4-space indents**.
- Write **docstrings** for functions.
- Keep functions **modular and reusable**.




---



## 🚀 **Get Started Today!**
👉 **Star this repo** to support the project!
👉 **Fork and contribute** to make fraud detection even better!

---
