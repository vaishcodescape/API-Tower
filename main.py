#API Tower
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_data():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}



