from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    otp_verified: bool

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class OTPVerify(BaseModel):
    email: EmailStr
    otp: str

class MovieCreate(BaseModel):
    title: str
    genre: str
    duration: int

class MovieResponse(BaseModel):
    id: str
    title: str
    genre: str
    duration: int

class TicketCreate(BaseModel):
    movie_id: str
    seat_number: str

class TicketResponse(BaseModel):
    id: str
    movie_id: str
    user_id: str
    seat_number: str
    booking_time: datetime
