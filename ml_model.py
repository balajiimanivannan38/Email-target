from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self):
        self.vec=TfidfVectorizer()
        self.clf=LogisticRegression()

    def train(self,data):
        X=self.vec.fit_transform([d["text"] for d in data])
        y=[d["label"] for d in data]
        self.clf.fit(X,y)

    def predict(self,text):
        return self.clf.predict(self.vec.transform([text]))[0]