from pydantic import BaseModel, EmailStr, model_validator
from typing import Dict

class patient(BaseModel):
    name:str
    age:int
    contact:Dict[str, str]
    email:EmailStr
    

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 65 and "emergency_contact" not in model.contact:
            raise ValueError("please add emergency contact")
        else:
            return model



def add_patient(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact)
    print(patient.email)
    print("data inserted")

patient_01 = {
    "name":"ali",
    "age":66,
    "contact":{"phone":"0213456789", "emergency_contact":"123456789"},
    'email':'abc@smiu.edu.pk'
    }

patient01 = patient(**patient_01)
add_patient(patient01)
