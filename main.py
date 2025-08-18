from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hello world"}

@app.get("/about")
def about():
    return {"about":"Hello I am Muhammad Hashir"}