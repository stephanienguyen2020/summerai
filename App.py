from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/send_message", response_class=JSONResponse)
async def send_message(message: Message):
    user_message = message.message

    # Rule-based response logic (can be replaced with more advanced logic)
    if 'change the date' in user_message.lower():
        response = "Yes, you can change the date of your reservation for up to seven days in advance. To do this, go to 'Your Reservations' and click the reservation. Then, go to 'Edit' and enter a new date."
    else:
        response = "I'm not sure how to help with that. Please contact support for more assistance."

    return {"reply": response}
