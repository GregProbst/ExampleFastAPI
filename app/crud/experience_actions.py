from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_experience_by_person_company(db: Session,
                                     person_id: int,
                                     company: str) -> models.Experience:
    return db.query(models.Experience).filter(models.Experience.person_id == person_id,
                                              models.Experience.company == company).first()


def create_experience(db: Session,
                      person_id: int,
                      experience: schemas.ExperienceBase) -> models.Experience:
    db_experience = models.Experience(company=experience.company,
                                      years=experience.years,
                                      description=experience.description,
                                      tech_used=experience.tech_used,
                                      person_id=person_id)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience
