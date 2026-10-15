from fastapi import FastAPI
from app.routers import diretores, filmes

app = FastAPI(
    title="API de Registro de Filmes",
    description="Projeto prático usando FastAPI, SQLAlchemy e Alembic.",
    version="1.0.0"
)


app.include_router(diretores.router)
app.include_router(filmes.router)

@app.get("/")
def home():
    return {"mensagem": "API de Registro de Filmes rodando com sucesso!"}