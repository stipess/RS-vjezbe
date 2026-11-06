import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)

class Podaci(BaseModel):
    firstname : str
    lastname : str

counter = -1
def choose_response():
    response = [
        "I SAID DON'T CLICK IT!",
        "You love breaking the rules, dont you?",
        "Ok, click it. I don't care.",
        "I hope you break your mouse.",
        "I am gonna report you."
    ]
    return response[counter]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/button")
async def return_button():
    global counter
    if counter >= 4:
        counter = 0
    else:
        counter += 1

    return {"message" : choose_response()}

@app.post("/addname")
async def addname(user_input : Podaci):
    print(user_input)