from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers import users, movies, tickets

app = FastAPI(title="Online Ticket Booking - FastAPI + MongoDB")

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # allow all headers
)

@app.get("/")
def root():
    return {"message": "Welcome to Online Ticket Booking API"}

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(tickets.router)
