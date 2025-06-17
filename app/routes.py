from fastapi import APIRouter
from .models import Item

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to FastAPI from bluescript!"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.post("/items/")
def create_item(item: Item):
    return {"item": item}

@router.get('/greet/{user}')
def greet_user(user:str = None):
    return {'message': f'Welcome {user if user else "Annonymous"}'}