from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"msg": "Auth route is working!"}