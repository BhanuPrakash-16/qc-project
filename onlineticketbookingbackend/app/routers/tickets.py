from fastapi import APIRouter
from .. import schemas, crud

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=schemas.TicketResponse)
async def book_ticket(ticket: schemas.TicketCreate):
    user_id = "dummy-user-id"  # Replace with JWT auth later
    return await crud.book_ticket(ticket, user_id)

@router.get("/")
async def get_tickets():
    return await crud.list_tickets()
