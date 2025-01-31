from fastapi import FastAPI, Path

app = FastAPI()

data = {
    1:{
        "name":"Laptop 1",
        "company": "Lenovo",
        "price": 1200
    },
    2:{
        "name":"Laptop 2",
        "company": "hp",
        "price": 1000
    },

    3:{
        "name":"Laptop 3",
        "company": "Dell",
        "price": 1400
    }
}

@app.get("/get_item/{item_id}")
def item(item_id: int = Path(..., description = "Enter Id of the product to access")):
    return data[item_id]