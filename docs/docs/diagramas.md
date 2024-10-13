# Diagramas

Esta seção apresenta diagramas que ilustram o fluxo de operações da API Nuvem, ajudando a compreender melhor o funcionamento interno e a interação entre os componentes.

## Diagrama de Sequência

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Database
    participant ExternalAPI

    User->>API: POST /registrar
    API->>Database: Inserir novo usuário
    Database-->>API: Confirmação
    API-->>User: 201 Created (JWT)

    User->>API: POST /login
    API->>Database: Verificar credenciais
    Database-->>API: Dados do usuário
    API-->>User: 200 OK (JWT)

    User->>API: GET /consultar
    API->>API: Validar JWT
    API->>ExternalAPI: Requisitar dados externos
    ExternalAPI-->>API: Dados externos
    API-->>User: 200 OK (Dados externos)
```

## Fluxograma de Autenticação

```mermaid
flowchart TD
    Start[Início] -->|Usuário envia credenciais| Login[Endpoint /login]
    Login -->|Credenciais válidas?| Check{Verificar no banco de dados}
    Check -->|Sim| GenerateToken[Gerar JWT]
    GenerateToken --> Response[Retornar JWT]
    Check -->|Não| Error[Retornar erro de autenticação]
```

## Diagrama de Arquitetura

```mermaid
graph LR
    subgraph Client Side
        User[Usuário]
    end
    subgraph Server Side
        API
        Database[(PostgreSQL)]
        ExternalAPI[(API Externa)]
    end

    User --> API
    API --> Database
    API --> ExternalAPI
```

## Notas sobre os Diagramas

•	**Diagrama de Sequência:** Mostra a interação temporal entre o usuário, a API, o banco de dados e a API externa durante as operações principais.

•	**Fluxograma de Autenticação:** Ilustra o processo de autenticação do usuário e geração do token JWT.

•	**Diagrama de Arquitetura:** Fornece uma visão geral dos componentes do sistema e suas interações.