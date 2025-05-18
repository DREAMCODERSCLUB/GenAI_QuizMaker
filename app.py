import streamlit as st
from src.quiz import generate_quiz, configure_gemini
import time

# Configure Gemini
configure_gemini()

# UI Setup
st.set_page_config(page_title="AI Quiz Master", layout="wide")
st.title("🎯 AI Quiz Generator")
st.caption("Powered by Gemini Flash")

# Sidebar Controls
with st.sidebar:
    st.header("Settings")
    topic = st.text_input("Quiz Topic", "Machine Learning")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    num_questions = st.slider("Number of Questions", 1, 20, 5)
    generate_btn = st.button("Generate Quiz")

# Main Content Area
if generate_btn:
    with st.spinner("Generating your quiz..."):
        start_time = time.time()
        
        try:
            quiz = generate_quiz(topic, difficulty, num_questions)
            
            # Display metrics
            gen_time = time.time() - start_time
            st.success(f"Generated {num_questions} questions in {gen_time:.2f}s")
            
            # Quiz Display
            st.subheader(f"Quiz: {topic} ({difficulty})")
            st.code(quiz, language="markdown")
            
            # Export Options
            # Single Download Button
            st.download_button(
                label="Download Quiz as Text",
                data=quiz,
                file_name=f"quiz_{topic.lower()}.txt",
                help="Save the quiz to a text file"
            )
                    
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API key and try again")

# Footer
st.divider()
st.markdown("""
<style>
footer {visibility: hidden;}
.st-emotion-cache-cio0dv {padding: 1rem;}
</style>
""", unsafe_allow_html=True)
