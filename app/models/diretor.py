from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Diretor(Base):
    __tablename__ = "diretores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    nacionalidade = Column(String)


    filmes = relationship("Filme", back_populates="diretor")