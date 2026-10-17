from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.diretor import Diretor
from app.schemas.diretor import DiretorCreate, DiretorUpdate, DiretorResponse

router = APIRouter(prefix="/diretores", tags=["Diretores"])

@router.post("/", response_model=DiretorResponse, status_code=status.HTTP_201_CREATED)
def criar_diretor(diretor: DiretorCreate, db: Session = Depends(get_db)):
    db_diretor = Diretor(**diretor.model_dump())
    db.add(db_diretor)
    db.commit()
    db.refresh(db_diretor)
    return db_diretor

@router.get("/", response_model=List[DiretorResponse])
def listar_diretores(db: Session = Depends(get_db)):
    return db.query(Diretor).all()

@router.get("/{diretor_id}", response_model=DiretorResponse)
def buscar_diretor(diretor_id: int, db: Session = Depends(get_db)):
    diretor = db.query(Diretor).filter(Diretor.id == diretor_id).first()
    if not diretor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Diretor não encontrado"
        )
    return diretor

@router.put("/{diretor_id}", response_model=DiretorResponse)
def atualizar_diretor(diretor_id: int, diretor_in: DiretorUpdate, db: Session = Depends(get_db)):
    diretor = db.query(Diretor).filter(Diretor.id == diretor_id).first()
    if not diretor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Diretor não encontrado"
        )
    
    dados_atualizacao = diretor_in.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizacao.items():
        setattr(diretor, campo, valor)

    db.commit()
    db.refresh(diretor)
    return diretor

