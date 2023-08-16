import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base) :
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True) 
    description = Column(String(300))
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)

class Vehicle(Base) :
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)   
    length = Column(Float, nullable=False)

class Character(Base) :
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)     
    description = Column(String(300))
    name = Column(String(50), nullable=False)
    gender = Column(String(50),nullable=False)
    birth_year = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    skin_color = Column(String(10),nullable=False)
    eye_color = Column(String(10),nullable=False)
    planet_id =  Column(Integer, ForeignKey(Planet.id))
    planet = relationship(Planet)
    vehicle_id = Column(Integer, ForeignKey(Vehicle.id))
    vehicle = relationship(Vehicle)

class User(Base) :
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)

class Favorite_planet(Base) :
    __tablename__= 'favorite_planet'
    id = Column(Integer, primary_key=True) 
    planet_id = Column(Integer, ForeignKey(Planet.id))
    planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User.id)

class Favorite_vehicle(Base) :
    __tablename__= 'favorite_vehicle'
    id = Column(Integer, primary_key=True) 
    vehicle_id = Column(Integer, ForeignKey(Vehicle.id))
    vehicle = relationship(Vehicle)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User.id)

class Favorite_character(Base) :
    __tablename__= 'favorite_character'
    id = Column(Integer, primary_key=True) 
    character_id = Column(Integer, ForeignKey(Character.id))
    character = relationship(Character)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User.id)

        
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
