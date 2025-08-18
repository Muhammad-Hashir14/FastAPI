from fastapi import FastAPI
import json

app = FastAPI()

def load_data(path):
    with open(path, "r") as f:
        data = json.load(f)
        return data

@app.get("/")
def home():
    return {"message":"Patient Management System"}

@app.get("/about")
def about():
    return {"about":"A Fully funtional API to manage patient records"}

@app.get("/view")
def view():
    return load_data("patients.json")