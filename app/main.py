from fastapi import FastAPI
from app.database import engine
from app.models import models
from app.routers import experience_router, interests_router, people_router

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(people_router.router)
app.include_router(experience_router.router)
app.include_router(interests_router.router)


@app.get("/")
def index():
    return {"message": "This is Greg Probst's example project. Visit localhost:/8000/docs to see the documentation"}
