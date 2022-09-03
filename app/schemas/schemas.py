from pydantic import BaseModel


class ExperienceBase(BaseModel):
    company: str
    years: float
    description: str
    tech_used: str


class Experience(ExperienceBase):
    exp_id: int
    person_id: int

    class Config:
        orm_mode = True


class InterestBase(BaseModel):
    name: str
    description: str


class Interest(InterestBase):
    int_id: int
    person_id: int

    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class Person(PersonBase):
    person_id: int
    experience: list[Experience] = []
    interests: list[Interest] = []

    class Config:
        orm_mode = True
