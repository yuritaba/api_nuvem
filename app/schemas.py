from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class Token(BaseModel):
    jwt: str

class User(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True