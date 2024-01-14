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
