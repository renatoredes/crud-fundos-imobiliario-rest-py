# 🏡 CRUD de Fundos Imobiliários

Este é um projeto de CRUD (Create, Read, Update, Delete) para gerenciar informações de Fundos Imobiliários. Ele oferece uma interface simples para realizar operações básicas em uma base de dados de Fundos Imobiliários.

## Funcionalidades

- **Cadastro de Fundos Imobiliários:** Adicione novos fundos imobiliários à sua base de dados.
- **Listagem de Fundos Imobiliários:** Veja todos os fundos cadastrados de forma fácil e organizada.
- **Atualização de Informações:** Edite detalhes de fundos existentes conforme necessário.
- **Exclusão de Fundos Imobiliários:** Remova fundos da base de dados.

## Requisitos

- 🐍 [Linguagem de Programação Utilizada, Ex: Python 3.8+](https://www.python.org/)
- 🚀 [Framework Utilizado, Flask](https://flask.palletsprojects.com/en/3.0.x/)
- 🗃️ [Banco de Dados, SQLite](https://www.sqlite.org/index.html)

## Como Usar configurações de Ambiente

1. **Instalação de Dependências:**
   ```pip install Flask```
   ```pip install Flask-SQLAlchemy``` 


3. Execute o Aplicativo:
```python app.py```
O servidor será iniciado em http://127.0.0.1:5000/

# Refatoração
* Branch: separar-logica-crud 
* Seguindo as boas práticas de programação orientada a objetos (POO)
* Pastas apropriadas para responsabilidade de cada arquivo
pastas. ```models, routes, app```
* Quebra de o código em arquivos separados com responsabilidades específicas para manter o código organizado, modular e de fácil manutenção.

```
projeto/
│
├── models/
│   ├── __init__.py
│   └── models.py
│
├── crud/
│   ├── __init__.py
│   └── crud_fiis.py
│
├── routes/
│   ├── __init__.py
│   └── app.py
│
└── run.py
```