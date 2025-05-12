from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.get("/login")
def login_info():
    return {"msg": "Please use POST to log in"}
