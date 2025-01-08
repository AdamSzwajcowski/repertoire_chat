from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from pydantic import BaseModel
from responsegenerator import ResponseGenerator
import time
from uuid import uuid4

# create BaseModel class for data validation
class UserInput(BaseModel):
    sentence: str

app = FastAPI()
user_sessions = {}
SESSION_TIMEOUT = 600  # 10 minutes

@app.get("/")
async def read_root():
    return {"message": "Root defined."}

@app.post("/generate-response/")
async def generate_response(user_input: UserInput, request: Request, response: Response, session_id: str = Cookie(None)):
    # delete inactive sessions to avoid resource leak
    current_time = time.time()
    keys_to_delete = []
    for sid, session in user_sessions.items():
        if current_time - session.last_activity > SESSION_TIMEOUT:
            keys_to_delete.append(sid)
    for sid in keys_to_delete:
        del user_sessions[sid]

    # Check if session_id cookie is present
    if not session_id or session_id not in user_sessions:
        # Create a new session
        session_id = str(uuid4())
        user_sessions[session_id] = ResponseGenerator()
        response.set_cookie(key="session_id", value=session_id)
    
    # Retrieve the session
    generator = user_sessions[session_id]
    generator.last_activity = current_time

    # Get the model's response
    try:
        response_text = generator.respond(user_input.sentence)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))