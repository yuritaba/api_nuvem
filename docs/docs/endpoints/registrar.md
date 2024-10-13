# Registro de Usuário

## Descrição

O endpoint de registro permite que novos usuários se cadastrem na aplicação. Ao se registrar, o usuário recebe um token JWT que pode ser usado para autenticação em outros endpoints protegidos.

## Detalhes do Endpoint

- **URL**: `/registrar`
- **Método HTTP**: `POST`
- **Autenticação**: Não requer autenticação
- **Headers**: `Content-Type: application/json`

## Estrutura da Requisição

### Corpo da Requisição (JSON)

```json
{
  "nome": "string",
  "email": "string",
  "senha": "string"
}
```

•	**nome:** Nome completo do usuário.

•	**email:** Endereço de e-mail válido e único.

•	**senha:** Senha para a conta do usuário (será armazenada de forma segura).

### Exemplo de Requisição

```bash
POST /registrar HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "nome": "Yuri Tabacof",
  "email": "yuri@example.com",
  "senha": "cloud123"
}
```


## Resposta de Sucesso

•	**Status Code:** 201 Created

•	**Corpo da Resposta (JSON):**
```json
{
  "jwt": "<token_jwt>"
}
```

•	**jwt:** Token JWT que pode ser usado para autenticação em endpoints protegidos.

## Respostas de Erro

•	**400 Bad Request:** Dados inválidos ou ausentes na requisição.

•	**409 Conflict:** E-mail já cadastrado.

### Exemplo de Resposta de Erro:

```json
{
  "detail": "E-mail já cadastrado."
}
```