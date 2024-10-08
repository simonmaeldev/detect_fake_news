import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
from typing import Union
from scipy.special import expit
from shared_models.prediction_models import PredictResponse

class FakeNewsDetector:
    def __init__(self, 
                 stop_words: Union[str, list] = 'english', 
                 max_df: float = 0.7, 
                 max_iter: int = 50, 
                 test_size: float = 0.2, 
                 random_state: int = 7):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=max_df)
        self.classifier = PassiveAggressiveClassifier(max_iter=max_iter)
        self.test_size = test_size
        self.random_state = random_state
        
    def train(self, csv_file: str) -> None:
        # Load and preprocess data
        df = pd.read_csv(csv_file)
        labels = df.label
        x_train, x_test, y_train, y_test = train_test_split(
            df['text'], labels, test_size=self.test_size, random_state=self.random_state
        )
        
        # Vectorize the text
        tfidf_train = self.vectorizer.fit_transform(x_train)
        tfidf_test = self.vectorizer.transform(x_test)
        
        # Train the classifier
        self.classifier.fit(tfidf_train, y_train)
        
        # Evaluate the model
        y_pred = self.classifier.predict(tfidf_test)
        score = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {round(score*100,2)}%')
        print(confusion_matrix(y_test, y_pred, labels=['FAKE','REAL']))
        
    def save_model(self, model_file: str) -> None:
        with open(model_file, 'wb') as file:
            pickle.dump((self.vectorizer, self.classifier), file)
    
    @classmethod
    def load_model(cls, model_file: str) -> 'FakeNewsDetector':
        detector = cls()
        with open(model_file, 'rb') as file:
            detector.vectorizer, detector.classifier = pickle.load(file)
        return detector
    
    def predict(self, text: str) -> PredictResponse:
        # Vectorize the input text
        tfidf_text = self.vectorizer.transform([text])
        
        # Get decision function scores
        decision_scores = self.classifier.decision_function(tfidf_text)
        
        # Convert decision scores to probabilities using sigmoid
        prob = expit(decision_scores)[0]
        
        # Make prediction
        # prediction = 'REAL' if prob > 0.5 else 'FAKE'
        prediction = prob > 0.5
        
        # Get confidence
        confidence = abs(prob - 0.5) * 2
        
        return PredictResponse(real=prediction, confidence=round(confidence * 100, 2)) 

# Example usage:
if __name__ == "__main__":
    # Training
    detector = FakeNewsDetector()
    detector.train('news.csv')
    detector.save_model('fake_news_model.pkl')
    
    # Loading and predicting
    loaded_detector = FakeNewsDetector.load_model('fake_news_model.pkl')
    sample_text = "This is a sample news article."
    prediction, probability = loaded_detector.predict(sample_text)
    print(f"The news is predicted to be: {prediction}")
    print(f"Probability: {probability:.2f}%")
