from passlib.hash import bcrypt
from .database import users_collection, movies_collection, tickets_collection
from .utils import generate_otp, send_email
from datetime import datetime
from bson import ObjectId

# ---- USER ----
async def create_user(user):
    hashed_pw = bcrypt.hash(user.password)
    otp = generate_otp()
    user_doc = {
        "username": user.username,
        "email": user.email,
        "password": hashed_pw,
        "otp": otp,
        "otp_verified": False
    }
    result = await users_collection.insert_one(user_doc)
    send_email(user.email, "Your OTP Code", f"Your OTP is {otp}")
    return {**user_doc, "id": str(result.inserted_id)}

async def verify_user_otp(email, otp):
    user = await users_collection.find_one({"email": email})
    if user and user["otp"] == otp:
        await users_collection.update_one({"email": email}, {"$set": {"otp_verified": True}, "$unset": {"otp": ""}})
        return True
    return False

async def login_user(email, password):
    user = await users_collection.find_one({"email": email})
    if user and bcrypt.verify(password, user["password"]):
        return {**user, "id": str(user["_id"])}
    return None

# ---- MOVIES ----
async def add_movie(movie):
    result = await movies_collection.insert_one(movie.dict())
    return {**movie.dict(), "id": str(result.inserted_id)}

async def list_movies():
    movies = await movies_collection.find().to_list(100)
    return [{**m, "id": str(m["_id"])} for m in movies]

# ---- TICKETS ----
async def book_ticket(ticket, user_id):
    ticket_doc = {
        "movie_id": ticket.movie_id,
        "user_id": user_id,
        "seat_number": ticket.seat_number,
        "booking_time": datetime.now()
    }
    result = await tickets_collection.insert_one(ticket_doc)
    return {**ticket_doc, "id": str(result.inserted_id)}

async def list_tickets():
    tickets = await tickets_collection.find().to_list(100)
    return [{**t, "id": str(t["_id"])} for t in tickets]
