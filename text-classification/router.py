from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

class ModelRouter:
    """Class to route the request to the appropriate model"""
    path = "search-query-trainer"
    model = None
    tokenizer = None
    class_map = {'LABEL_0':'ft', 'LABEL_1':'mr', 'LABEL_2':'ct', 'LABEL_3':'pkg', 'LABEL_4':'ch', 'LABEL_5':'cnc'}
    def _load_files(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(self.path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.path)

    def predict(self, text: str):
        if not text:
            return "NA"
        clf = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer)
        response = clf.predict(text)
        if isinstance(response, list):
            return self.class_map.get(response[0]["label"], "NA")
        return "NA"
    
    def startup_event(self):
        self._load_files()

