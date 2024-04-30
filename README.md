# Fast Zero

## Live application: 
  - https://fast-zero-app.fly.dev/docs

## Sobre o projeto: 
Esta api foi desenvolvida para criar lista de tarefas de usuários, permitindo um controle através de uma interface RESTful. 

## Estrutura de pastas 
/fast_zero Código-fonte principal da aplicação 
  /routes Definição das rotas da api
/migrations Migrações do banco de dados 
/tests Testes automatizados garantindo a qualidade

## Tecnologias utilizadas 
- **Alembic**: ferramenta de migração para uso em conjunto com o SQLAlchemy
- **Docker**: para desacoplamento de infraestrutura com uso de virtualização
- **Docker-compose**: Para orquestração da aplicação multi-container 
- **FastAPI**: framework web para a construção de APIs com Python
- **Pgadmin**: ferramenta de gestão do PostgreSQL
- **PostgreSQL**: SGBD objeto relacional
- **Pydantic**: Biblioteca de validação de código
- **Pytest**: para os testes unitários
- **Python**: utilizando o paradigma orientado a objetos
- **SQLAlchemy**: biblioteca de ORM

## Rodando localmente
Clone o repositório
```bash
  git clone https://github.com/pedroarthuralvesdeoliveira/fast_zero/ 
```

Se utiliza Windows, tenha certeza de ter o [WSL]([url](https://learn.microsoft.com/pt-br/windows/wsl/install)) instalado  

[Baixe]([url](https://docs.docker.com/get-docker/)) o docker desktop

[Instale]([url](https://docs.docker.com/compose/install/)) o docker compose

Inicialize os serviços
```bash
  docker-compose up
```

## Funcionalidades
Auth
  - **Atualizar token de acesso**
  - **Login para autenticação**

Todos
  - **Atualizar tarefa**
  - **Criar tarefa**
  - **Deletar tarefa**
  - **Listar tarefa**

Usuário
  - **Atualizar usuário**
  - **Autenticar usuário**
  - **Criar usuário**
  - **Deletar usuário**
  - **Listar usuário**
  - **Listar todos os usuários**
  - **Verificar se usuário existe**
