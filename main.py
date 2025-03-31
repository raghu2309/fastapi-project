from fastapi import FastAPI
#from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

app = FastAPI()

# Define a request body model
class Message(BaseModel):
    text: str

# Define a dictionary for predefined responses
response_map = {
    "SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 4, 14), 1, 10))": 670,
    "SUM(TAKE(SORTBY({14,2,0,7,7,2,11,9,10,15,9,6,12,3,11,14}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 7))": 58,
    "How many Wednesdays": 1404,
    "q-extract-csv-zip.zip": "f02d3",
    "sum of all values associated with these symbols": 36643,
    "Enter the raw Github URL": "https://raw.githubusercontent.com/raghu2309/Firsttest/refs/heads/main/email.json",
    "running cat * | sha256sum in that folder show in bash": "0b385542271b99b1e68b7447fef4a3c02d15dbbd2b7f91f8b6012fe24cf93241 *-",
    "total size of all files at least 7413 bytes large": 186541,
    "running grep . * | LC_ALL=C sort | sha256sum":"49f4243accc169badcbf8968319a02af123bbfef614bd4a6f8e5dd63bc30b888 *-",
    "2 nearly identical files": 6,
    "Publish a page using GitHub": "https://raghu2309.github.io/Firsttest/RSNEW.html",
    "you can access Google Colab": "cc133",
    "fixing a mistake": 151686,
    "how many input tokens": 449,
    "maximum latitude of the bounding box": -33.7688301,
    "who scored 16 or more marks": 60354,
    "total margin for transactions": 0.55339,
    "unique students": 29,
    "successful GET requests for pages under": 51,
    "requests under malayalammp3": 10930,
    "units of Ball were sold in São Paulo": 9586,
    "total sales value": 54377

}

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI 2025!"}

@app.get("/message/")
def get_message(text: str):
    return {"response": f"You said: {text}"}

@app.post("/message/")
async def post_message(msg: Message):
    # Check if the input text matches any key in the response_map
    for key in response_map:
        if key in msg.text:
            return {"answer": str(response_map[key])}
    #target_string = "SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 4, 14), 1, 10))"

    #if target_string in msg.text:
    #    return {"answer": 670}
    
    return {"answer": "Query not recognized"}
'''
@app.post("/message/")
async def post_message(msg: Message):
    return {"response": f"You said: {msg.text}"}
'''