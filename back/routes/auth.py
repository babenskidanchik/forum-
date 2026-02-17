from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from back.database import SessionLocal, User
import bcrypt

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#registration
@router.post('/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='User already exists')
    hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    new_user = User(username=user.username, password_hash=hashed.decode())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created"}

#enter
@router.post('/login')
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not bcrypt.checkpw(data.password.encode(), user.password_hash.encode()):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}