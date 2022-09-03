from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database
from app.schemas import schemas
from app.models import models
from app.crud import interests_actions

router = APIRouter(
    tags=["Interests"]
)


@router.post("/people/{person_id}/interest",
             response_model=schemas.Interest,
             status_code=status.HTTP_201_CREATED)
def create_interest(person_id: int,
                    interest: schemas.InterestBase,
                    db: Session = Depends(database.get_db)) -> models.Interest:
    interest_check = interests_actions.get_interest_by_name_person(db=db,
                                                                   interest_name=interest.name,
                                                                   person_id=person_id)
    if interest_check:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Person with ID of {person_id} already has an interest called '{interest.name}'")
    return interests_actions.create_interest(db=db, person_id=person_id, interest=interest)
