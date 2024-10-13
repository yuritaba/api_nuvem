# Autenticação de Usuário

## Descrição

O endpoint de login autentica um usuário existente e retorna um token JWT para acesso aos endpoints protegidos.

## Detalhes do Endpoint

- **URL**: `/login`
- **Método HTTP**: `POST`
- **Autenticação**: Não requer autenticação
- **Headers**: `Content-Type: application/json`

## Estrutura da Requisição

### Corpo da Requisição (JSON)

```json
{
  "email": "string",
  "senha": "string"
}
```

•	**email:** Endereço de e-mail do usuário cadastrado.

•	**senha:** Senha correspondente à conta do usuário.

### Exemplo de Requisição

```bash
POST /login HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "email": "yuri@example.com",
  "senha": "cloud123"
}
```

## Resposta de Sucesso

•	**Status Code:** 200 OK

•	**Corpo da Resposta (JSON):**

```json
{
  "jwt": "<token_jwt>"
}
```

•	**jwt:** Token JWT para autenticação em endpoints protegidos.

## Respostas de Erro

•	**401 Unauthorized:** Credenciais inválidas.

Exemplo de Resposta de Erro

```json
{
  "detail": "E-mail ou senha incorretos."
}
```