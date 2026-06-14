from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/", response_model=List[Item])
def list_items(available: Optional[bool] = None):
    if available is None:
        return items
    return [item for item in items if item.available == available]
