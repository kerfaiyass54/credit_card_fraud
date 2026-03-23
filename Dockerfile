FROM python:3.11-slim

WORKDIR /ccf-app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python /visualize/visualize_data.py && python main.py