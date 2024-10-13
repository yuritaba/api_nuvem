from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from database import SessionLocal, engine
import models, schemas, auth
from dados import obter_dados_externos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBearer()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

# Endpoint de Registro de Usuário
@app.post("/registrar", response_model=schemas.Token)
def registrar(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    hashed_senha = auth.gerar_hash_senha(user.senha)
    new_user = models.User(nome=user.nome, email=user.email, hashed_senha=hashed_senha)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = auth.criar_acesso_token(data={"sub": new_user.email})
    return {"jwt": token}

# Endpoint de Autenticação de Usuário
@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verificar_senha(user.senha, db_user.hashed_senha):
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")
    token = auth.criar_acesso_token(data={"sub": db_user.email})
    return {"jwt": token}

# Dependência para obter o usuário atual
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    email = auth.decodificar_token(token)
    if email is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credenciais inválidas")
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuário não encontrado")
    return user

# Endpoint de Consulta de Dados
@app.get("/consultar")
def consultar(user: models.User = Depends(get_current_user)):
    dados = obter_dados_externos()
    return dados