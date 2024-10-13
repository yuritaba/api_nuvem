# Instalação

Esta seção fornece instruções detalhadas sobre como configurar e executar a aplicação localmente usando o Docker e o Docker Compose.

## Pré-requisitos

- **Docker** instalado na máquina.
- **Docker Compose** instalado na máquina.
- **Git** para clonar o repositório.
- **Arquivo `.env`** com as variáveis de ambiente necessárias.

## Passos para Instalação

### 1. Clonar o Repositório

Clone o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/yuritabacof/api_nuvem.git
cd api_nuvem
```

### 2. Criar o Arquivo .env

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

```bash
DATABASE_URL=postgresql://postgres:cloud@database:5432/db_nuvem
SECRET_KEY=uma_chave_secreta_segura

POSTGRES_USER=postgres
POSTGRES_PASSWORD=cloud
POSTGRES_DB=db_nuvem
```

### 3. Executar o Docker Compose

Inicie os containers da aplicação e do banco de dados:

```bash
docker-compose up
```

Este comando irá:

•	Construir as imagens Docker necessárias.

•	Iniciar os containers definidos no docker-compose.yaml.

•	Configurar a rede interna para comunicação entre os containers.

### 4. Acessar a Aplicação

Após os containers estarem em execução, acesse a documentação interativa da API no seu navegador:

•	**Swagger UI:** http://localhost:8000/docs

### 5. Parar a Aplicação

Para parar os containers em execução, pressione Ctrl+C no terminal onde o Docker Compose está rodando ou execute:

```bash
docker-compose down
```