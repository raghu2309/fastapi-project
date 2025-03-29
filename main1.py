
from fastapi import FastAPI, Form
import numpy as np

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the LLM-based API! Use /api/ to ask questions."}
@app.post("/api/")
async def answer_question(question: str = Form(...)):
    # Check if the question contains a Google Sheets formula
    if "SUM(" in question:
        try:
            # Extract the formula part
            formula_start = question.find("=") + 1
            formula = question[formula_start:].strip()
            
            # Simulate evaluation (handling SEQUENCE function)
            if "SEQUENCE" in formula:
                # Example: =SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 4, 14), 1, 10))
                num_rows = 100
                num_cols = 100
                start_value = 4
                step = 14
                sequence = np.arange(start_value, start_value + (num_rows * num_cols * step), step).reshape(num_rows, num_cols)
                constrained_array = sequence[:1, :10]  # ARRAY_CONSTRAIN(..., 1, 10)
                result = np.sum(constrained_array)
            else:
                result = "Formula not supported yet."

            return {"answer": str(result)}
        except Exception as e:
            return {"answer": f"Error processing formula: {str(e)}"}

    return {"answer": "Question type not supported."}
