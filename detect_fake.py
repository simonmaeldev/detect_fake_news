import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

class FakeNewsDetector:
    def __init__(self, 
                 stop_words='english', 
                 max_df=0.7, 
                 max_iter=50, 
                 test_size=0.2, 
                 random_state=7):
        self.vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=max_df)
        self.classifier = PassiveAggressiveClassifier(max_iter=max_iter)
        self.test_size = test_size
        self.random_state = random_state
        
    def train(self, csv_file):
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
        
    def save_model(self, model_file):
        with open(model_file, 'wb') as file:
            pickle.dump((self.vectorizer, self.classifier), file)
    
    @classmethod
    def load_model(cls, model_file):
        detector = cls()
        with open(model_file, 'rb') as file:
            detector.vectorizer, detector.classifier = pickle.load(file)
        return detector
    
    def predict(self, text):
        # Vectorize the input text
        tfidf_text = self.vectorizer.transform([text])
        
        # Make prediction
        prediction = self.classifier.predict(tfidf_text)
        
        # Get confidence score
        confidence = self.classifier.decision_function(tfidf_text)
        
        # The confidence score is a single value for binary classification
        # Positive values indicate the 'REAL' class, negative values indicate the 'FAKE' class
        confidence_score = abs(confidence[0])
        
        return prediction[0], confidence_score

# Example usage:
if __name__ == "__main__":
    # Training
    detector = FakeNewsDetector()
    detector.train('news.csv')
    detector.save_model('fake_news_model.pkl')
    
    # Loading and predicting
    loaded_detector = FakeNewsDetector.load_model('fake_news_model.pkl')
    sample_text = "This is a sample news article."
    prediction, confidence = loaded_detector.predict(sample_text)
    print(f"The news is predicted to be: {prediction}")
    print(f"Confidence score: {confidence:.4f}")
