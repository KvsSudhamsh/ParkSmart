from sqlalchemy.orm import Session
from models import User, ParkingSpot, Reservation

def create_user(db: Session, username:str, password:str):
    new_user = User()
    new_user.Username = username
    new_user.Password = password
    # new_user = User(username = username, password = password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_spots(db: Session):
    return db.query(ParkingSpot).all()

def set_spots(db: Session, totalSpots : int):
    existingSpots = db.query(ParkingSpot).count()

    if totalSpots > existingSpots:
        for i in range(existingSpots + 1, totalSpots + 1):
            newSpot = ParkingSpot(id = i, status = "available")
            db.add(newSpot)
        db.commit()
        return {"message": f"{totalSpots - existingSpots} spots added successfully."}
    return {"message": "No new spots are added. Total spots already meet or exceed the required count."}

def reserve_spot(db: Session, user_id:int, spot_id:int):
    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id).first()
    if spot and spot.status == "available":
        spot.status = "reserved"
        reservation = Reservation(user_id = user_id, spot_id = spot_id)
        db.add(reservation)
        db.commit()
        db.refresh(reservation)
        return reservation
    return None