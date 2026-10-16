from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    
    
    diretor_id = Column(Integer, ForeignKey("diretores.id"), nullable=False)

    
    diretor = relationship("Diretor", back_populates="filmes")