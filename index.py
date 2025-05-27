from flask import Flask, render_template, request
import joblib
import re
import nltk
nltk.data.path.append("nltk_data")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in stop_words]
    return ' '.join(review)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        message = request.form['message']
        cleaned = preprocess(message)
        vect = vectorizer.transform([cleaned]).toarray()
        result = model.predict(vect)[0]
        prediction = "Spam" if result == 1 else "Ham"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

