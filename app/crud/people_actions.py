from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_person(db: Session,
               person_id: int) -> models.Person:
    return db.query(models.Person).filter(models.Person.person_id == person_id).first()


def get_all_people(db: Session):
    return db.query(models.Person).all()


def get_person_by_name(db: Session,
                       first_name: str,
                       last_name: str) -> list[models.Person]:
    return db.query(models.Person).filter(models.Person.first_name == first_name,
                                          models.Person.last_name == last_name).all()


def get_person_by_email(db: Session,
                        email: str) -> models.Person:
    return db.query(models.Person).filter(models.Person.email == email).first()


def create_person(db: Session,
                  person: schemas.PersonBase) -> models.Person:
    db_person = models.Person(first_name=person.first_name,
                              last_name=person.last_name,
                              email=person.email)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
