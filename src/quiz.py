import google.generativeai as genai
import os

def configure_gemini():
    genai.configure(api_key=os.getenv("____________________"))    #Add your api key

def generate_quiz(topic, difficulty="Medium", num_questions=5):
    """Generate MCQs using Gemini"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""Generate {num_questions} {difficulty}-level MCQs about {topic}:
    - Format each question clearly
    - Include 4 plausible options
    - Mark the correct answer
    - Add brief explanations
    
    Template:
    Question: [Question text]
    A) [Option A]
    B) [Option B]
    C) [Option C]
    D) [Option D]
    Answer: [Correct letter]
    Explanation: [1-2 sentences]
    """
    
    response = model.generate_content(prompt)
    return response.text
