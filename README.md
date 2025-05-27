# SMS Spam Classifier 🚫📨✅

This is a simple web application that classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques.

👉 **Live Demo**: [https://smsspam-ck3s.onrender.com](https://smsspam-ck3s.onrender.com)

---

## 🚀 Features

- Text classification using **TF-IDF vectorization**
- Built with **Flask** for backend
- Trained using **Logistic Regression** model
- Deployed using **Render**

---

## 🧠 How it works

1. User enters an SMS message.
2. The message is preprocessed (lowercased, punctuation removed, etc.).
3. Features are extracted using **TF-IDF (Term Frequency - Inverse Document Frequency)**.
4. The model predicts whether it's **Spam** or **Not Spam**.

---

## 🛠 Tech Stack

- Python 🐍
- Flask 🌐
- Scikit-learn 🤖
- NLP preprocessing
- TF-IDF vectorizer
- Render (for deployment)

---

## 🧪 How to Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/smsspam.git
   cd smsspam
   Create virtual environment and install dependencies:


python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Run the app:
  python index.py
