from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"data":"testing"}

@app.get("/about")
def about():
    return {"data":"about"}