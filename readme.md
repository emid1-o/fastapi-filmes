# API de Gestão e Registro de Filmes

API RESTful desenvolvida em Python utilizando FastAPI, SQLAlchemy e Alembic para gerenciamento de diretores e seus respectivos filmes. O projeto foi estruturado em camadas (core, models, schemas e routers) e utiliza migrações para controle do schema do banco de dados.

## 1. Modelo de Negócio

O sistema representa o relacionamento entre diretores de cinema e filmes:
- Um diretor pode ter vários filmes cadastrados.
- Cada filme é obrigatoriamente associado a um diretor.

## 2. Entidades e Relacionamentos

### Entidades e Atributos

1. **diretores**
   - `id`: Integer (Chave primária, auto-incremento)
   - `nome`: String (Obrigatório)
   - `nacionalidade`: String (Opcional)

2. **filmes**
   - `id`: Integer (Chave primária, auto-incremento)
   - `titulo`: String (Obrigatório)
   - `ano_lancamento`: Integer (Obrigatório)
   - `diretor_id`: Integer (Chave estrangeira para `diretores.id`)

### Relacionamento e Regras

- Relacionamento de 1 para N (1:N) configurado via `relationship` do SQLAlchemy.
- Validação de integridade: ao tentar cadastrar um filme, o sistema verifica se o `diretor_id` informado existe no banco. Caso não exista, é retornado erro `404`.

```
+-------------------+             +-----------------------+
|     diretores     |             |        filmes         |
+-------------------+             +-----------------------+
| id (PK)           |<----+       | id (PK)               |
| nome              |     |       | titulo                |
| nacionalidade     |     +-------| diretor_id (FK)       |
+-------------------+  (1)   (N)  | ano_lancamento        |
                                  +-----------------------+
```

## 3. Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior
- Git

### Passos para instalação e execução

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd fastapi-filmes
   ```

2. Crie e ative o ambiente virtual:
   - Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

5. Inicie o servidor da aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Acesse a documentação Swagger:
   Navegue até `http://127.0.0.1:8000/docs` no seu navegador.

## 4. Endpoints da API

### Diretores (`/diretores`)

| Método | Endpoint | Descrição | Status Code |
| --- | --- | --- | --- |
| `POST` | `/diretores/` | Cadastra um diretor | `201` |
| `GET` | `/diretores/` | Lista todos os diretores | `200` |
| `GET` | `/diretores/{id}` | Busca um diretor por ID | `200` |
| `PUT` | `/diretores/{id}` | Atualiza dados do diretor | `200` |
| `DELETE` | `/diretores/{id}` | Remove um diretor | `204` |

### Filmes (`/filmes`)

| Método | Endpoint | Descrição | Status Code |
| --- | --- | --- | --- |
| `POST` | `/filmes/` | Cadastra um filme (valida `diretor_id`) | `201` |
| `GET` | `/filmes/` | Lista todos os filmes | `200` |
| `GET` | `/filmes/{id}` | Busca um filme por ID | `200` |
| `PUT` | `/filmes/{id}` | Atualiza dados do filme | `200` |
| `DELETE` | `/filmes/{id}` | Remove um filme | `204` |

## 5. Tecnologias Utilizadas

- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Pydantic
- Uvicorn