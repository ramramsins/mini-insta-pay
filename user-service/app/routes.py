from fastapi import APIRouter, HTTPException
from app.models import UserRegister, UserLogin
from app.database import users_collection
from passlib.hash import bcrypt

router = APIRouter()

@router.get("/")
def root():
    return {"msg": "User Service is running"}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/register")
def register(user: UserRegister):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")
    
    users_collection.insert_one({
        "username": user.username,
        "email": user.email,
        "password": user.password  # Hash this in production
    })
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not bcrypt.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"msg": f"Welcome {db_user['username']}"}

@router.get("/login")
def login_info():
    return {"msg": "Please use POST to log in"}