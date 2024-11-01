import anthropic
import json
from fastapi import FastAPI
from dotenv import load_dotenv
from .prompt import generate_prompt

load_dotenv()

app = FastAPI()

client = anthropic.Anthropic()

@app.get("/")
def read_root():
    return {"win": "hology"}

@app.get("/v1/gi/{food_name}")
def read_item(food_name: str):
    message = generate_prompt(food_name=food_name, client=client)
    return json.loads(message.content[0].text)