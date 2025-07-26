import streamlit as st
from newspaper import Article
import joblib

# Load model and vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorization.pkl")

# Streamlit UI
st.title("🔗 Fake News Detector from URL")
st.write("Enter a news article URL. The app will extract the content and check if it’s fake or real.")

url = st.text_input("Paste URL here:")

if st.button("Analyze"):
    if not url.strip():
        st.warning("Please enter a valid URL.")
    else:
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text

            if not text.strip():
                st.error("Could not extract any meaningful content from this URL.")
            else:
                st.info("✅ Article extracted successfully. Analyzing...")
                vectorized = vectorizer.transform([text])
                prediction = model.predict(vectorized)[0]

                result = "✅ Real News" if prediction == 1 else "🚫 Fake News"
                st.subheader(result)

        except Exception as e:
            st.error(f"❌ Failed to fetch or parse the article. Error: {e}")

# import streamlit as st

# st.title("Test App")
# st.write("If you're seeing this, Streamlit works fine!")
