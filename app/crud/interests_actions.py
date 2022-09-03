from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_interest_by_name_person(db: Session,
                                person_id: int,
                                interest_name: str) -> models.Interest:
    return db.query(models.Interest).filter(models.Interest.person_id == person_id,
                                            models.Interest.name == interest_name).first()


def create_interest(db: Session,
                    person_id: int,
                    interest: schemas.InterestBase) -> models.Interest:
    db_interest = models.Interest(name=interest.name,
                                  description=interest.description,
                                  person_id=person_id)
    db.add(db_interest)
    db.commit()
    db.refresh(db_interest)
    return db_interest
