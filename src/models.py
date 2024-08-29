import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

class User(db.Model):
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    user_favorites = db.relationship('Favorites', backref='user', lazy=True)
    def serialize(self):
        return {
            'userId': self.userId,
            'userName': self.userName,
            'email': self.email
        }




class Character(db.Model):
    __tablename__ = 'character'
    characterId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    character_favorites = db.relationship('Favorites', backref='character', lazy=True)
    
    def serialize(self):
        return {
            'characterId': self.characterId,
            'name': self.name,
            'species': self.species,
            'gender': self.gender,
            'height': self.height,
            'weight': self.weight,
            'age': self.age
        }

    


class Planet(db.Model):
    __tablename__ = 'planet'
    planetId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    population = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    rotationPeriod = db.Column(db.Integer)
    orbitalPeriod = db.Column(db.Integer)
    climate = db.Column(db.String(25))


    planet_favorites = db.relationship('Favorites', backref='planet', lazy=True)


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicleId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    vehicleClass = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(25))
    passengers = db.Column(db.Integer)
    loadCapacity = db.Column(db.Integer)
 
def serialize(self):
        return {
            'vehicleId': self.vehicleId,
            'name': self.name,
            'vehicleClass': self.vehicleClass,
            'model': self.model,
            'passengers': self.passengers,
            'loadCapacity': self.loadCapacity
        }
    
vehicle_favorites = db.relationship('Favorites', backref='vehicle', lazy=True)

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)
    characterId = db.Column(db.Integer, db.ForeignKey('character.characterId'), nullable=False)
    planetId = db.Column(db.Integer, db.ForeignKey('planet.planetId'), nullable=False)
    vehicleId = db.Column(db.Integer, db.ForeignKey('vehicle.vehicleId'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'characterId': self.characterId,
            'planetId': self.planetId,
            'vehicleId': self.vehicleId
        }

    def to_dict(self):
        return {}

## Generate the ER diagram
render_er(Base, 'diagram.png')
