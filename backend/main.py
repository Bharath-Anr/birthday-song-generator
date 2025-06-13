from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app= FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

#CORS Setup
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

#input model
class UserAnswers(BaseModel):
    answers:list[str]

#post endpoint 
@app.post("/generate-song")
async def generate_song(data: UserAnswers):
    name=data.answers[0]
    age=data.answers[1]
    color=data.answers[2]
    hobby=data.answers[3]
    friend=data.answers[4]
    food=data.answers[5]
    pet=data.answers[6]
    place=data.answers[7]
    memory=data.answers[8]
    wish=data.answers[9]

    prompt=f"""
        Generate a joyful birthday song in simple English.
        Make it a bit offensive,roasting,cheerful and rhyming using the given details.Try to use all of this information and give me a funny 12 line song:
        What’s your friend’s full name and how old are they turning? {name}
        If your friend was a color, what color would they be and why?: {age}
        What’s your friend’s favorite hobby or something they do all the time? {color}
        Who is your friend’s best buddy, and what’s a funny memory they share?{hobby}
        What’s your friend’s favorite food they can’t live without? {friend}
        If your friend could visit any place right now, where would it be? {food}
        What’s a recent funny or happy moment your friend had? {pet}
        What’s a quirky or adorable habit your friend has that you notice? {place}
        What’s a funny nickname or joke people have for your friend? {memory}
       What’s a silly or embarrassing moment your friend secretly enjoys? {wish} """
    
    response = requests.post(
    "https://api.sarvam.ai/v1/chat/completions",
    headers={
        "api-subscription-key": "sk_zx28olbd_glswkKZVr78wLKimu0IrpRZN"
    },
    json={
        "messages": [
        {
            "content": prompt,
            "role": "user"
        }
        ],
        "model": "sarvam-m"
    },
    )

    od=response.json()
    content=od["choices"][0]["message"]["content"]
    print(content)

     # Clean and filter the quotes
    #quotes = [q.strip("-•0123456789. ") for q in quotes if q.strip()]
    return {"quotes": content}