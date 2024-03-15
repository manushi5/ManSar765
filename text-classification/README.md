## Query Category Prediction

The solution has two major parts: Data Science Model and Prediction Service API

### Data Science Model

1. Using huggingface[pytorch] library, I use a pretrained bert model and train on the given labeled data using Google colab GPU.
2. The data contains some noisy queries which are removed in the data processing step.
3. The model is evaluated using class wise confusion matrix.

### Prediction API

1. The Rest API is built using FastAPI library and packaged using docker.
2. To run the service, you need to download the weights file and put it in `search-query-trainer/`path: [File Weights](https://drive.google.com/file/d/1NQYkEMkzHK0wT0xNm9pAm3XfGVmOn9xY/view?usp=drive_link)
3. To run the service locally, run the following commands:
- make docker-build-serve
- make docker-run-serve
