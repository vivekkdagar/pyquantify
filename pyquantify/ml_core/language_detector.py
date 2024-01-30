import warnings
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import joblib  # Import the joblib library for model serialization


class LanguageDetector:
    def __init__(self, source):
        self.le = LabelEncoder()
        self.cv = CountVectorizer()
        self.model = MultinomialNB()
        self.X = None
        self.y = None
        self.data_list = list()
        self.dataset = source

    def wake(self):
        warnings.simplefilter("ignore")
        data = pd.read_csv("Language Detection.csv")
        data["Language"].value_counts()
        self.X = data["Text"]
        self.y = data["Language"]

        for text in self.X:
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)
            self.data_list.append(text)

    def train(self):
        self.y = self.le.fit_transform(self.y)
        self.X = self.cv.fit_transform(self.data_list).toarray()
        x_train, x_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.20)
        self.model.fit(x_train, y_train)

    def save_model(self, filename="model.joblib"):
        joblib.dump((self.le, self.cv, self.model), filename)

    def load_model(self, filename="model.joblib"):
        self.le, self.cv, self.model = joblib.load(filename)

    def predict(self):
        x = self.cv.transform([self.dataset]).toarray()
        lang = self.model.predict(x)
        lang = self.le.inverse_transform(lang)
        return lang[0]

    def __str__(self):
        return self.predict()
