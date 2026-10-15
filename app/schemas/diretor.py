from typing import Optional
from pydantic import BaseModel


class DiretorBase(BaseModel):
    nome: str
    nacionalidade: Optional[str] = None


class DiretorCreate(DiretorBase):
    pass


class DiretorUpdate(BaseModel):
    nome: Optional[str] = None
    nacionalidade: Optional[str] = None


class DiretorResponse(DiretorBase):
    id: int

    class Config:
        from_attributes = True  