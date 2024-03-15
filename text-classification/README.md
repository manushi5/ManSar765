## Text Classification

The solution has two major parts: Data Science Model and Prediction Service API.

### Data Science Model

1. Using huggingface[pytorch] library, I use a pretrained bert model and train on the given labeled data using Google colab GPU. The pretrained bert model is a good match for the given problem since it is fine tuned for sequence classification tasks such as text categorization. The only weights that will be updated during training are the weights of the classification head (the final layer) that is added on top of the pre-trained BERT model.
2. The data contains some noisy queries which are removed in the data processing step.
3. The model is evaluated using class wise confusion matrix along with classwise precision/recall/F1 score metrics.

### Prediction API

1. The Rest API is built using FastAPI library and packaged using docker.
2. To run the service, you need to download the weights file and put it in `search-query-trainer/`path: [File Weights](https://drive.google.com/file/d/1NQYkEMkzHK0wT0xNm9pAm3XfGVmOn9xY/view?usp=drive_link)
3. To run the service locally, run the following commands:
- make docker-build-serve
- make docker-run-serve

### Future Work

1. I would re-run the model evaluation on a larger data set to make sure the metrics are stable.
2. I would spend time on error analysis to understand the misclassified cases.
3. If deploying pytorch model is problematic, ..... 
