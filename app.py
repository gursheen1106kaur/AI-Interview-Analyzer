import streamlit as st
import os

from utils import analysis
from utils.speech import transcribe_audio
from utils.scoring import calculate_score, score_feedback

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Interview Analyzer",
    page_icon="🎤",
    layout="wide"
)

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("🎤 AI Interview Analyzer")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🎤 Analyze Interview", "ℹ️ About"]
)

# ==========================================
# Home Page
# ==========================================

if page == "🏠 Home":

    st.title("🎤 AI Interview Analyzer")

    st.header("Analyze Your Interview Performance Using AI")

    st.write(
        "This application helps users improve their interview skills "
        "by analyzing speech, sentiment, confidence, and communication."
    )

    st.subheader("✨ Features")

    st.markdown("""
- 🎙️ Speech-to-Text
- 😊 Sentiment Analysis
- 🗣️ Filler Word Detection
- ⏱️ Speaking Speed Analysis
- 🏆 Overall Interview Score
""")

# ==========================================
# Analyze Interview Page
# ==========================================

elif page == "🎤 Analyze Interview":

    st.title("🎤 Analyze Interview")

    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=["wav", "mp3", "m4a"]
    )

    if uploaded_file is not None:

        # ----------------------------------
        # Save Uploaded File
        # ----------------------------------

        st.success("✅ Audio uploaded successfully!")

        st.audio(uploaded_file)

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # ----------------------------------
        # Speech-to-Text
        # ----------------------------------

        st.subheader("📝 Transcript")

        with st.spinner("🤖 AI is analyzing your interview..."):
         
           transcript = transcribe_audio(file_path)
         
        st.success("✅ Analysis completed successfully!")

        st.write(transcript)
#==========================================
#Interview Statistics
#==========================================
        st.subheader("📊 Interview Statistics")

        word_count = analysis.count_words(transcript)

        duration = analysis.get_audio_duration(file_path)

        wpm = analysis.calculate_wpm(word_count, duration)

        sentiment, confidence = analysis.analyze_sentiment(transcript)

        status, feedback = analysis.speaking_speed_feedback(wpm)

        # ----------------------------------
        # Sentiment Analysis
        # ----------------------------------

    

        st.subheader("😊 Sentiment Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Sentiment", sentiment)

        with col2:
            st.metric("Confidence", f"{confidence:.2f}%")

        

        # ----------------------------------
        # Word Count & Duration
        # ----------------------------------

        st.subheader("📊 Speech Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Words", word_count)

        with col2:
            st.metric("Duration", f"{duration:.2f} sec")

        # ----------------------------------
        # Speaking Speed
        # ----------------------------------

        st.subheader("⚡ Speaking Speed")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Words Per Minute", f"{wpm:.2f}")

        with col2:
            st.metric("Status", status)

        st.info(feedback)

        # ----------------------------------
        # Filler Word Detection
        # ----------------------------------

        filler_result = analysis.detect_filler_words(transcript)

        st.subheader("🗣️ Filler Word Analysis")

        filler_result = analysis.detect_filler_words(transcript)

        total_fillers = sum(filler_result.values())

        if total_fillers == 0:

            st.success("🎉 No filler words used!")

        else:

            filler_data = {
                    "Filler Word": [],
                    "Count": []
        }

        for word, count in filler_result.items():

            if count > 0:
                filler_data["Filler Word"].append(word)
                filler_data["Count"].append(count)

        st.table(filler_data)

        # ----------------------------------
        # Overall Interview Score
        # ----------------------------------

        score = calculate_score(wpm, total_fillers)

        score_status, feedback_text = score_feedback(score)

        st.subheader("🏆 Overall Interview Score")

        st.metric("Score", f"{score}/100")

        st.progress(score / 100)

        st.write(f"### {score_status}")

        st.info(feedback_text)

# ==========================================
# About Page
# ==========================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.write("""
AI Interview Analyzer is an AI-powered application that helps users
practice interviews by analyzing their recorded answers.

### Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- TextBlob
- Machine Learning
- Natural Language Processing (NLP)
- PyDub
""")