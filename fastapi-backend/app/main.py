# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float

# # Sample data
# items = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Phone", "price": 500},
#     {"name": "Phone", "price": 500},
#     {"name": "Phone", "price": 500}
# ]

# # GET endpoint
# @app.get("/")
# def read_items():
#     return items

# # POST endpoint
# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item.dict())
#     return item

# # GET by ID
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return items[item_id] if item_id < len(items) else {"error": "Item not found"}    

from fastapi import FastAPI
app=FastAPI(title='cyber security API')
@app.get("/")
def health_check():
     return {"status": "Server is running"}




