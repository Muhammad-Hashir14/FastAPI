from pydantic import BaseModel

class Address(BaseModel):
    area: str
    city: str
    state: str
    pincode :int

class Patient(BaseModel):
    name:str
    age:int
    gender:str
    address:Address

address01 = {
    "area":"Saddar",
    "city":"karachi",
    "state":"sindh",
    "pincode":7000
    }
address = Address(**address01)

patient1 = {
    "name":"Ali",
    "age":34,
    "gender":"Male",
    "address":address
}

patient1 = Patient(**patient1)
print(patient1.name)
print(patient1.address)
print(f"{patient1.address.area}, {patient1.address.city}, {patient1.address.state}, {patient1.address.pincode}")