from pydantic import BaseModel, EmailStr, field_validator

class patient(BaseModel):
    name:str
    age:int
    contact:str
    email:EmailStr

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['smiu.edu.pk','iu.edu.pk']
        domain=value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError("you are not eligible")
        else:
            return value
    
    @field_validator("name")
    @classmethod
    def upper_name(cls, value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def convertfloat(cls, value):
        return float(value)

def add_patient(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact)
    print(patient.email)
    print("data inserted")

patient_01 = {
    "name":"ali",
    "age":45,
    "contact":"021231232",
    'email':'abc@smiu.edu.pk'
    }

patient01 = patient(**patient_01)
add_patient(patient01)
