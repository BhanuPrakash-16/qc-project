from fastapi import APIRouter, HTTPException
from .. import schemas, crud

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=schemas.UserResponse)
async def register_user(user: schemas.UserCreate):
    new_user = await crud.create_user(user)
    return {
        "id": new_user["id"],
        "username": new_user["username"],
        "email": new_user["email"],
        "otp_verified": new_user["otp_verified"]
    }

@router.post("/verify")
async def verify_otp(data: schemas.OTPVerify):
    success = await crud.verify_user_otp(data.email, data.otp)
    if not success:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    return {"message": "OTP verified successfully"}

@router.post("/login", response_model=schemas.UserResponse)
async def login(user: schemas.UserLogin):
    db_user = await crud.login_user(user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not db_user["otp_verified"]:
        raise HTTPException(status_code=403, detail="Email not verified")
    return {
        "id": db_user["id"],
        "username": db_user["username"],
        "email": db_user["email"],
        "otp_verified": db_user["otp_verified"]
    }
