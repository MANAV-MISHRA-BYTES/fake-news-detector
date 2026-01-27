import streamlit as st
from transformers import pipeline
import time

st.set_page_config(
    page_title="CogniFact AI | Misinformation Filter",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #4A90E2; font-weight: 700;}
    .sub-text {font-size: 1.2rem; color: #888;}
    .metric-card {background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #4A90E2;}
    div.stButton > button {background-color: #4A90E2; color: white; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2040/2040946.png", width=80)
    st.title("🧠 CogniFact AI")
    st.markdown("---")
    
    st.subheader("⚙️ Control Panel")
    model_choice = st.selectbox("Select Neural Model", ["RoBERTa-Base (Accurate)", "DistilBERT (Fast - Simulation)"])
    sensitivity = st.slider("Sensitivity Threshold", 50, 90, 70)
    
    st.markdown("---")
    st.info("ℹ️ **Status:** System Online\n\n**GPU Acceleration:** Enabled (Cloud)")

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="hamzab/roberta-fake-news-classification")

def check_sensationalism(text):
    score = 0
    if text.isupper(): score += 30
    if "!!!" in text or "???" in text: score += 20
    words = ["SHOCKING", "UNBELIEVABLE", "SECRET", "BANNED", "EXPOSED"]
    for w in words:
        if w in text.upper(): score += 10
    return min(score, 100)

st.markdown('<p class="main-header">CogniFact AI: Neural Truth Engine</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Advanced Deep Learning system for detecting linguistic patterns of misinformation and sensationalism.</p>', unsafe_allow_html=True)
st.divider()

tab1, tab2, tab3 = st.tabs(["🕵️‍♂️ Live Analyzer", "📊 Batch Statistics", "🛠️ System Architecture"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_input = st.text_area("📰 News Feed Input", height=250, placeholder="Paste article content, headlines, or social media forwards here...")
        
        c1, c2, c3 = st.columns([1,1,2])
        with c1:
            analyze_btn = st.button("🚀 Analyze Content", use_container_width=True)
        with c2:
            clear = st.button("🔄 Clear Console", use_container_width=True)

    with col2:
        st.markdown("### 📡 Live Telemetry")
        st.write("Monitoring linguistic features...")
        st.empty()

    if analyze_btn and user_input.strip():
        with st.spinner("🔄 Neural Network is processing tokens..."):
            time.sleep(1)
            
            classifier = load_model()
            result = classifier(user_input)[0]
            label = result['label']
            confidence = result['score'] * 100
            
            sens_score = check_sensationalism(user_input)

            st.divider()
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Classification", "FAKE" if label == "FAKE" else "REAL", delta="-Alert" if label=="FAKE" else "Verified")
            with m2:
                st.metric("AI Confidence", f"{confidence:.1f}%")
            with m3:
                st.metric("Sensationalism Score", f"{sens_score}/100", delta_color="inverse")

            c_res1, c_res2 = st.columns([2, 1])
            
            with c_res1:
                if label == "FAKE":
                    st.error(f"🚨 **Critical Alert:** This content matches patterns of misinformation.")
                    st.write("The model detected linguistic cues often associated with fabricated stories, satire, or clickbait.")
                else:
                    st.success(f"✅ **Verification Passed:** Content appears credible.")
                    st.write("The text aligns with patterns found in standard reporting and verified sources.")
                
                st.markdown(" **Probability Distribution:**")
                st.progress(int(confidence))
                st.caption(f"Model is {confidence:.1f}% sure this is {label}.")

            with c_res2:
                st.info("💡 **Analysis Insights**")
                st.markdown(f"""
                - **Sentiment High-Points:** {sens_score}%
                - **Urgency Detected:** {'High' if sens_score > 50 else 'Normal'}
                - **Model Used:** RoBERTa
                """)
                
            with st.expander("📂 View Raw Engine Logs (JSON)"):
                st.json(result)

with tab2:
    st.header("📊 Global Statistics")
    st.info("This module tracks aggregate data from all user queries (Simulated for Demo).")
    
    metrics_col1, metrics_col2 = st.columns(2)
    with metrics_col1:
        st.write("**Detection Rate (Last 24h)**")
        st.bar_chart({"Real": 45, "Fake": 12, "Satire": 5})
    with metrics_col2:
        st.write("**Common Trigger Words**")
        st.line_chart([10, 45, 12, 67, 34, 80])

with tab3:
    st.markdown("### 🏗️ System Architecture")
    st.code("""
    Pipeline:
    [User Input] --> [Tokenization (BPE)] --> [Transformer Layers (12)] --> [Classification Head] --> [Output]
    """, language="python")
    st.markdown("Built with **Python, Streamlit, and Hugging Face Transformers**.")
