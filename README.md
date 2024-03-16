# API Transporte Público

Este projeto é uma API de transporte público que permite aos usuários consultar informações sobre linhas de transporte, horários e lotação dos veículos.

## Funcionalidades

- Consultar todas as rotas disponíveis
- Adicionar uma nova rota
- Atualizar informações de uma rota existente
- Remover uma rota

## Como executar

1. Clone o repositório:

```
git clone [URL_DO_REPOSITORIO]
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Configurar variáveis de ambiente:

Copie o arquivo .env.example para um novo arquivo chamado .env e ajuste as variáveis conforme necessário.

4. Execute a aplicação:

```
python app.py
```

## Endpoints

A API fornece os seguintes endpoints:

- GET /transporte: Lista todas as rotas
- POST /transporte: Adiciona uma nova rota
- PUT /transporte/<id>: Atualiza uma rota existente pelo ID
- DELETE /transporte/<id>: Remove uma rota pelo ID

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

## Interface da Aplicação

Aqui está uma visão da nossa aplicação em ação:

![api-transporte-publico](https://github.com/SheylaSilvana/api-transporte-publico/assets/57454583/1d719855-5288-4f54-81f1-368bc56de19f)

