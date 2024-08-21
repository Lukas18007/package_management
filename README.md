# Package Management API

Esta é uma API desenvolvida com Django e Django Rest Framework para gerenciar pacotes de medicação (`Package`). A API permite atualizar o status de autorização dos pacotes com base em diferentes condições de risco fazendo uma análise desse risco.

## Funcionalidades

- **Atualização de Status do Pacote**: A API permite que o status de autorização de um pacote seja atualizado com base no status recebido e no nível de risco associado ao pacote.

## Estrutura da Model `Package`

A model `Package` possui os seguintes campos:

- `id`: Chave primária do pacote.
- `description`: Descrição do pacote.
- `authorized`: Indica se o pacote foi autorizado (`True` ou `False`).
- `authorized_at`: Data em que o pacote foi autorizado.
- `risk`: Nível de risco associado ao pacote (`B`, `M`, `A`).

## Regras de Autorização

A API suporta três tipos de status de aprovação:

1. **Aprovado**:
   - O campo `authorized` é atualizado para `True`, independentemente do nível de risco.
   - O campo `authorized_at` é atualizado com a data atual.

2. **Aprovado com apontamentos**:
   - Se o nível de risco (`risk`) for `B` ou `M`, o campo `authorized` é atualizado para `True` e o campo `authorized_at` é atualizado com a data atual.
   - Caso contrário, `authorized` é atualizado para `False`.

3. **Reprovado**:
   - O campo `authorized` é atualizado ou permanece como `False`.

## Endpoints

### Atualizar Status de Autorização

Atualiza o status de autorização de um pacote com base no status fornecido.

- **URL**: `/package/authorize/<int:id>/`
- **Método HTTP**: `PATCH`
- **Corpo da Requisição**:
  ```json
  {
    "status": "aprovado"
  }
