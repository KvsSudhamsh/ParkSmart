from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    _username = Column(String, unique=True, nullable=True)
    _password = Column(String, nullable=False)

    @property
    def Username(self):
        return self._username

    @Username.setter
    def Username(self, username):
        self._username = username
        return None

    @property
    def Password(self):
        return self._password
    
    @Password.setter
    def Password(self, password):
        self._password = password
        return None

class ParkingSpot(Base):
    __tablename__ = 'parking_spots'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default='available')

class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    spot_id = Column(Integer, ForeignKey('parking_spots.id'))
