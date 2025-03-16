from fastapi import FastAPI, Query
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key="AIzaSyAkD4V20xHXMBZkwBDhNfynMc9JZXcKbcg")

@app.get("/generate_questions/")
def generate_questions(
    exam: str = Query("UPSC", description="Enter the exam name"),
    subject: str = Query("General Studies", description="Enter the subject name"),
    num_questions: int = Query(5, description="Number of questions to generate")
):
    prompt = f"""
    You are an expert in {exam} exam question generation. 
    Generate {num_questions} high-quality questions for the subject {subject}.
    Cover important topics and ensure they are exam-relevant.
    """
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)
    
    return {"exam": exam, "subject": subject, "questions": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






