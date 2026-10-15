from typing import Optional
from pydantic import BaseModel
from app.schemas.diretor import DiretorResponse


class FilmeBase(BaseModel):
    titulo: str
    ano_lancamento: int
    diretor_id: int


class FilmeCreate(FilmeBase):
    pass


class FilmeUpdate(BaseModel):
    titulo: Optional[str] = None
    ano_lancamento: Optional[int] = None
    diretor_id: Optional[int] = None


class FilmeResponse(FilmeBase):
    id: int
    diretor: Optional[DiretorResponse] = None  

    class Config:
        from_attributes = True