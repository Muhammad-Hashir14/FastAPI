from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/patient/{patient_id}")
def patient(patient_id: str=Path(...,description= "ID of the patient in the DB", example="1")):
    """
    get patient by id
    Path to provide user how to enter patient id with a description
    HTTPException with proper status code of error
    """

    data = load_data("patients.json")
    if patient_id in data:
        return data[patient_id]
    else:
        return HTTPException(status_code=404, detail = "Patient not found")
    
@app.get("/sort")
def sort(
    sort_by: str=Query(..., descrption="Sort by height, weight or bmi"), 
    order_by:str=Query('asc',description="order data in asc or desc")):

    fields = ["height", "weight", "bmi"]
    if sort_by not in fields:
        HTTPException(status_code=400,detail=f"{sort_by} does not exist in db")
    if order_by not in ["asc", "desc"]:
        HTTPException(status_code=400, detail="ordery can be asc or desc")
    
    data = load_data("patients.json")

    BOOL = True if order_by == "desc" else False

    sorted_data = sorted(list(data.values()), key=lambda x: x.get(sort_by, 0), reverse=BOOL)
    return sorted_data  