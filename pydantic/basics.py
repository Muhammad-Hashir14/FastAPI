from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=40, title="Name of the Patient", description="Give the name of the paient less than 40 chars", examples=["ali", "ahmed"])]
    email : Optional[EmailStr]
    linkedin : Optional[AnyUrl]
    age : int = Field(gt=0, lt=120) 
    weight : Annotated[float, Field(gt=0, strict=True)]
    married: bool=True
    allergies : Annotated[Optional[List[str]],Field(max_length=5, default=None)]
    contact : Dict[str, str]

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("data inserted")

patient1 = {"name":"ali", "age":13, "weight":40.4, "married": False, "allergies":["Dust"], "contact":{"phone":"123456789"}}
patient2 = {"name":"umer", "age":21, "weight":54.4, "contact":{"phone":"935234234"}}

patient1 = Patient(**patient1)
patient2 = Patient(**patient2)


insert_patient(patient1)
insert_patient(patient2)
