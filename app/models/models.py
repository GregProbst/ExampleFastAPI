from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = "people"

    person_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

    experience = relationship("Experience", back_populates="person")
    interests = relationship("Interest", back_populates="person")


class Experience(Base):
    __tablename__ = "experiences"

    exp_id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    years = Column(Float)
    description = Column(String)
    tech_used = Column(String)
    person_id = Column(Integer, ForeignKey("people.person_id"))

    person = relationship("Person", back_populates="experience")


class Interest(Base):
    __tablename__ = "interests"

    int_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    person_id = Column(Integer, ForeignKey("people.person_id"))

    person = relationship("Person", back_populates="interests")
