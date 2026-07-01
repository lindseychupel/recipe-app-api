Recipe App API

API REST desenvolvida com Python, Django e Django REST Framework para gerenciamento de receitas, ingredientes e tags. O projeto foi estruturado com foco em boas práticas de backend, testes automatizados, containerização com Docker e deploy em ambiente AWS.

Sobre o projeto

Desenvolvi esta API com a proposta de construir uma base sólida para aplicações backend que precisam de autenticação, modelagem relacional, organização de regras de negócio e exposição de endpoints REST. A aplicação permite gerenciar receitas com título, descrição, tempo de preparo, preço, link de referência, ingredientes, tags e imagem.[2][3]

Além da parte funcional, também dei atenção à organização do projeto, qualidade de código e previsibilidade do ambiente. Por isso, a aplicação utiliza PostgreSQL, Docker, testes automatizados e lint, o que ajuda a manter o desenvolvimento mais consistente e próximo de um cenário real.[2][4]

Funcionalidades

- Autenticação de usuários.
- CRUD de receitas.
- CRUD de tags.
- CRUD de ingredientes.
- Associação de tags e ingredientes às receitas.
- Upload de imagens para receitas.
- Filtros por tags e ingredientes.
- Estrutura preparada para documentação da API.

Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- Pillow
- drf-spectacular
- uWSGI
- AWS
- Flake8
- Django Test Framework.

Estrutura

O projeto foi dividido por responsabilidades para facilitar manutenção e evolução do código:

- `app/core/`: models, admin, comandos e componentes centrais.
- `app/user/`: autenticação, serializers e endpoints de usuário.
- `app/recipe/`: regras de negócio, serializers, views e rotas das receitas.
- `tests/`: testes de models, autenticação, endpoints e fluxos principais.

Essa separação ajuda a manter a aplicação mais legível e torna mais simples expandir novas funcionalidades.

Como executar:

- Clonar o repositório:

git clone <url-do-repositorio>
cd recipe-app-api

- Subir os containers:


docker-compose up --build


- Aplicar as migrações:


docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"


- Criar superusuário


docker-compose run --rm app sh -c "python manage.py createsuperuser"

Testes e qualidade

Os testes cobrem os comportamentos principais da aplicação, incluindo autenticação, models, endpoints e regras relacionadas a receitas, ingredientes, tags e upload de imagem. Isso me ajudou a evoluir o projeto com mais segurança e validar o comportamento esperado da API ao longo do desenvolvimento.

- Para rodar os testes:


docker-compose run --rm app sh -c "python manage.py test"


- Para rodar o lint:


docker-compose run --rm app sh -c "flake8"


Documentação da API

A documentação da API foi preparada com `drf-spectacular`, biblioteca usada para geração de schema OpenAPI em projetos com Django REST Framework, ela facilita manter a documentação alinhada com a API real e pode ser integrada com Swagger UI e outras ferramentas de leitura de schema. Com a aplicação em execução, a documentação pode ser disponibilizada pelas rotas configuradas no projeto.

Deploy

A aplicação também foi pensada para execução fora do ambiente local, com ambiente containerizado e estrutura adequada para publicação em nuvem. O deploy em AWS complementa o projeto ao mostrar não só a implementação da API, mas também a preocupação com entrega, padronização de ambiente e execução em infraestrutura.

Endpoints principais

Os recursos centrais da API incluem:

- Usuários
- Autenticação
- Receitas
- Tags
- Ingredientes
- Upload de imagens para receitas.

Considerações finais

Este projeto representa bem a forma como gosto de trabalhar backend: foco em organização, clareza, testes e construção de uma base que possa crescer sem perder legibilidade. Mais do que entregar endpoints funcionando, a ideia aqui foi estruturar uma API consistente, fácil de manter e pronta para evoluir.
