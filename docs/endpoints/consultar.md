# Consulta de Dados Externos

## Descrição

Este endpoint permite que usuários autenticados consultem dados externos de uma API de terceiros, por exemplo, previsão do tempo.

## Detalhes do Endpoint

- **URL**: `/consultar`
- **Método HTTP**: `GET`
- **Autenticação**: Requer autenticação via token JWT
- **Headers**:
  - `Authorization: Bearer <token_jwt>`

## Parâmetros de Consulta

- **opcional**: Dependendo da implementação, você pode permitir parâmetros adicionais na URL para filtrar os dados.

## Exemplo de Requisição

```bash
GET /consultar HTTP/1.1
Host: localhost:8000
Authorization: Bearer <token_jwt>
```

## Resposta de Sucesso:

•	Status Code: 200 OK

•	Corpo da Resposta (JSON):

```json
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
```

•	**data:** Dados retornados da API externa. Temperatura máxima e mínima dos últimos 7 dias.

## Respostas de Erro

•	**401 Unauthorized:** Token JWT inválido ou ausente.

•	**500 Internal Server Error:** Erro ao consultar a API externa.

Exemplo de Resposta de Erro

```json
{
  "detail": "Token de autenticação inválido."
}
```