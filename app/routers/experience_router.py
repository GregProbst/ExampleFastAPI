from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.models import models
from ..schemas import schemas
from app.crud import experience_actions

router = APIRouter(
    tags=["Experience"]
)


@router.post("/people/{person_id}/experience",
             response_model=schemas.Experience,
             status_code=status.HTTP_201_CREATED)
def create_experience(person_id: int,
                      experience: schemas.ExperienceBase,
                      db: Session = Depends(database.get_db)) -> models.Experience:
    exp = experience_actions.get_experience_by_person_company(db=db, person_id=person_id, company=experience.company)
    if exp:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Person ID '{person_id}' already has experience at '{experience.company}'")
    return experience_actions.create_experience(db=db, person_id=person_id, experience=experience)

