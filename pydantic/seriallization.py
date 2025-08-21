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


temp = patient1.model_dump()

print(type(temp))
print(temp)

temp_include = patient1.model_dump(include=["name","age"])
print(temp_include)

temp_exclude = patient1.model_dump(exclude=["name", "gender"])
print(temp_exclude)

temp_json = patient1.model_dump_json(include=["name", "age", "address"])
print(temp_json)
print(type(temp_json))