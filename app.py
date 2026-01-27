import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Veritas AI: Fake News Detector", page_icon="🔍")

@st.cache_resource
def load_model():
    classifier = pipeline("text-classification", model="hamzab/roberta-fake-news-classification")
    return classifier

st.title("🔍 Veritas AI: Fake News Detector")
st.markdown("""
    **Problem:** Misinformation spreads quickly, making it hard for students to verify facts.
    **Solution:** Paste a news headline or article excerpt below to assess its credibility using AI.
""")

user_input = st.text_area("Enter News Text Here:", height=150, placeholder="e.g., 'Aliens have landed in New York City...'")

if st.button("Analyze Credibility"):
    if user_input.strip():
        with st.spinner("Analyzing text patterns..."):
            try:
                classifier = load_model()
                result = classifier(user_input)[0]
                label = result['label']
                score = result['score']
                st.divider()
                if label == 'FAKE':
                    st.error(f"🚨 **Potential Fake News Detected**")
                    st.progress(score)
                    st.caption(f"Confidence: {score*100:.2f}%")
                    st.write("This text matches patterns commonly found in misinformation or satire.")
                else:
                    st.success(f"✅ **Likely Real News**")
                    st.progress(score)
                    st.caption(f"Confidence: {score*100:.2f}%")
                    st.write("This text aligns with patterns found in reliable news reporting.")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to analyze.")
st.divider()
st.markdown("Powered by **Hugging Face Transformers** & **Streamlit** | Model: RoBERTa")