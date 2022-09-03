from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import database
from app.models import models
from app.schemas import schemas
from app.crud import people_actions

#
router = APIRouter(
    tags=["People"]
)


@router.get("/people/",
            response_model=List[schemas.Person])
def get_all_people(db: Session = Depends(database.get_db)) -> list[models.Person]:
    return people_actions.get_all_people(db)


@router.get("/person/",
            response_model=List[schemas.Person])
def get_person_by_name(first_name: str,
                       last_name: str,
                       db: Session = Depends(database.get_db)) -> list[models.Person]:
    person = people_actions.get_person_by_name(db=db, first_name=first_name, last_name=last_name)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Person with name: '{first_name} {last_name}' was not found")
    return person


@router.post("/person/",
             response_model=schemas.Person,
             status_code=status.HTTP_201_CREATED)
def create_person(person: schemas.PersonBase,
                  db: Session = Depends(database.get_db)) -> models.Person:
    new_person = people_actions.get_person_by_email(db=db, email=person.email)
    if new_person:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Person with e-mail address '{person.email}' already exists")
    return people_actions.create_person(db=db, person=person)


@router.get("/person/{person_id}",
            response_model=schemas.Person)
def get_person_by_id(person_id: int,
                     db: Session = Depends(database.get_db)) -> models.Person:
    person = people_actions.get_person(db=db, person_id=person_id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Person with ID of '{person_id}' not found")
    return person
