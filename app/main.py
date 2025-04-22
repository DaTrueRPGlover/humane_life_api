from fastapi import FastAPI
from app.routes import auth, meallog

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(meallog.router, prefix="/meallog", tags=["Meal Logs"])