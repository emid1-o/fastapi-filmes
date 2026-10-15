from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.diretor import Diretor
from app.models.filme import Filme
from app.schemas.filme import FilmeCreate, FilmeUpdate, FilmeResponse

router = APIRouter(prefix="/filmes", tags=["Filmes"])

@router.post("/", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    
    diretor_existe = db.query(Diretor).filter(Diretor.id == filme.diretor_id).first()
    if not diretor_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não é possível cadastrar o filme: Diretor com ID {filme.diretor_id} não existe."
        )

    db_filme = Filme(**filme.model_dump())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

@router.get("/", response_model=List[FilmeResponse])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(Filme).all()

@router.get("/{filme_id}", response_model=FilmeResponse)
def buscar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )
    return filme

@router.put("/{filme_id}", response_model=FilmeResponse)
def atualizar_filme(filme_id: int, filme_in: FilmeUpdate, db: Session = Depends(get_db)):
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )

    dados_atualizacao = filme_in.model_dump(exclude_unset=True)

  
    if "diretor_id" in dados_atualizacao:
        novo_diretor_id = dados_atualizacao["diretor_id"]
        diretor_existe = db.query(Diretor).filter(Diretor.id == novo_diretor_id).first()
        if not diretor_existe:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Diretor com ID {novo_diretor_id} não existe."
            )

    for campo, valor in dados_atualizacao.items():
        setattr(filme, campo, valor)

    db.commit()
    db.refresh(filme)
    return filme

@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if not filme:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )
    
    db.delete(filme)
    db.commit()
    return None