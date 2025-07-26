
# 🔎 Fake News Detector from URL 📰

Detect whether a news article is **real** or **fake** by simply pasting its URL.  
This web app uses **machine learning** and **natural language processing** to analyze the content and predict its authenticity.

---

## 🚀 Features

- 🔗 Accepts **URL input** to fetch article content
- 🤖 Trained on a labeled dataset 
- ✅ Lightweight & works in real-time 

---

## 🧠 How It Works

1. Paste a news article URL
2. The app scrapes article text 
4. A trained ML model classifies it as **Fake** or **Real**

---

## 📁 Project Structure

```
fake-news-app/
├── app.py                  # Streamlit frontend
└── models/
    ├── fake_news_model.pkl     # Trained model
    └── vectorization.pkl       # TF-IDF vectorizer
```

---

## ⚙️ Installation & Run Locally

### 1. Clone this repo:

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

### 2. Install requirements:

```bash
pip install -r requirements.txt
```

> Sample `requirements.txt`:
```
streamlit
scikit-learn
pandas
newspaper3k
joblib
```

### 3. Run Streamlit app:

```bash
streamlit run app.py
```


## ✨ Credits

- Built by [Bhoomi](https://github.com/Bhoomi-112/)
- UI powered by [Streamlit](https://streamlit.io/)

---
