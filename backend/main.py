from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from models import Base
from sqlalchemy.orm import Session
from crud import create_user, get_spots, reserve_spot

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, password)

@app.get("/spots")
def list_spots(db: Session = Depends(get_db)):
    return get_spots(db)

@app.post("/reserve")
def make_reservation(user_id: int, spot_id: int, db: Session = Depends(get_db)):
    reservation = reserve_spot(db, user_id, spot_id)
    if reservation:
        return {"message": "Reservation successful"}
    return HTTPException(status_code=400, detail= "Spot not available")