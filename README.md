# Yuri Tabacof - API nuvem
## API RESTful com FastAPI, PostgreSQL e Docker

### 1. Explicação do Projeto

Este projeto consiste em uma **API RESTful** desenvolvida com **FastAPI**, utilizando **PostgreSQL** como banco de dados e **Docker** para containerização. A API permite o cadastro, autenticação de usuários e consulta de dados externos relacionados ao clima.

A aplicação está dockerizada e foi publicada no **Docker Hub**, permitindo fácil acesso e replicação do ambiente de desenvolvimento e produção.

### 2. Explicação de Como Executar a Aplicação

#### Pré-requisitos:
- **Docker** e **Docker Compose** instalados na máquina.
- **Arquivo `.env`** configurado com as variáveis de ambiente corretas.

#### Passos para executar a aplicação:

1. **Clone este repositório**:

2. **Crie o arquivo .env com as seguintes variáveis de ambiente**:
DATABASE_URL= url para o seu db postgres, exemplo: postgresql://postgres:cloud@database:5432/db_nuvem
SECRET_KEY= uma_chave_secreta_aleatoria, exemplo: bea8aeaa507d4571165a852131f3d5fd95767633bc419df13c7f9bb060a07294
POSTGRES_USER= seu usuario postgres aqui
POSTGRES_PASSWORD= sua senha postgres aqui
POSTGRES_DB= nome do seu db postgres aqui

3. **Execute o Docker Compose para iniciar os containers da aplicação e do banco de dados:**:

4. **Acesse a aplicação no navegador em http://localhost:8000/docs para visualizar a documentação da API através do Swagger UI**:

### 3. Documentação dos Endpoints da API

1. **Registro de Usuário**:

- Método: POST
- Endpoint: /registrar
- Descrição: Cria um novo usuário e retorna um token JWT.
- Exemplo de Requisição:
{
  "nome": "João da Silva",
  "email": "joaozinho@example.com",
  "senha": "cloud123"
}
- Resposta:
{
  "jwt": "<token_jwt>"
}

2. **Autenticação de Usuário**:

- Método: POST
- Endpoint: /login
- Descrição: Autentica um usuário existente e retorna um token JWT.
- Exemplo de Requisição:
{
  "email": "joaozinho@example.com",
  "senha": "cloud123"
}
- Resposta:
{
  "jwt": "<token_jwt>"

}

2. **Consulta de dados externos**:

- Método: GET
- Endpoint: /consultar
- Descrição: Consulta dados externos de uma API de terceiros, no caso dados sobre o clima dos últimos sete dias (temperatura máxima e mínima).
- Exemplo de Requisição:
Header: Authorization: Bearer <JWT>
- Resposta:
{
  "time": [
    "2024-10-13",
    "2024-10-14",
    "2024-10-15",
    "2024-10-16",
    "2024-10-17",
    "2024-10-18",
    "2024-10-19"
  ],
  "temperature_2m_max": [
    26.3,
    25.4,
    27.6,
    28.9,
    29.4,
    30.8,
    21
  ],
  "temperature_2m_min": [
    15.9,
    16.1,
    15.7,
    15.9,
    18,
    18.1,
    19.3
  ]
}

link para o docker hub do projeto: https://hub.docker.com/r/yuritabacof/api_nuvem
