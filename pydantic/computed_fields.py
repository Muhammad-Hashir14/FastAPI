from pydantic import BaseModel, EmailStr, computed_field

class patient(BaseModel):
    name:str
    age:int
    contact:str
    email:EmailStr
    height: float
    weight : float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi
    


def add_patient(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact)
    print(patient.email)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print("data inserted")

patient_01 = {
    "name":"ali",
    "age":45,
    "contact":"021231232",
    'email':'abc@smiu.edu.pk',
    'height': 6.2,
    'weight':80.1
    }

patient01 = patient(**patient_01)
add_patient(patient01)
