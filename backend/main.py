from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from responsegenerator import ResponseGenerator
import time

# create BaseModel class for data validation
class UserInput(BaseModel):
    sentence: str
    
app = FastAPI()
user_sessions = {}
SESSION_TIMEOUT = 600   # 10 minutes

@app.get("/")
async def read_root():
    return {"message": "Root defined."}

@app.post("/generate-response/")
async def generate_response(user_input: UserInput, request: Request):
    
    # delete inactive sessions to avoid resource leak
    current_time = time.time()
    for ip, session in user_sessions.items():
        if current_time - session.last_activity > SESSION_TIMEOUT: del user_sessions[ip] 
    
    # get user's IP
    user_ip = request.headers.get("X-Forwarded-For")
    
    # get the current session (initiate first if not created yet)
    if user_ip not in user_sessions:
        user_sessions[user_ip] = ResponseGenerator()
    generator = user_sessions[user_ip]
    generator.last_activity = current_time
 
    # get the model's response
    try:
        response = generator.respond(user_input.sentence)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# run app using Uvicorn (in terminal)
# uvicorn main:app --reload
