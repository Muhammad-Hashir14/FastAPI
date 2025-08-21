from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Give id of patient", examples=["1","2","3"])]
    name:Annotated[str, Field(..., description="Give name of the patient", examples=["Ali", "Ahsan"])]
    age:Annotated[int, Field(..., gt=0, le=120,description="Give age of patient", examples=[24,54,23])]
    gender:Annotated[str, Literal["male", "female", "others"], Field(..., description="give gender of the patient", examples=["male", "female"])]
    weight:Annotated[float, Field(...,description="Give weight of patient in kgs", examples=[60.0, 40.5])]
    height:Annotated[float, Field(...,description="Give height of the patient in meters", examples=[4.6,5.6])]
    medical_condition:Annotated[Optional[str], Field(default=None, description="Give medical condition of patient", examples=["hypertension"])]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi= round(self.weight * (self.height**2),2)
        return bmi


app = FastAPI()

def load_data(path):
    with open(path, "r") as f:
        data = json.load(f)
        return data
    
def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data,f)


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
def patient(patient_id: str=Path(...,description= "ID of the patient in the DB", examples="1")):
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

@app.post("/create")
def create_patient(patient:Patient):

    data = load_data("patients.json")
    if patient.id in data:
        raise HTTPException(status_code=400, detail = "patient already exists")
    
    data[patient.id] = patient.model_dump(exclude=["id"])
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "data saved successfully"})
