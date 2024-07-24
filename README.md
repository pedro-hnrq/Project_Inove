
<h1 align="center"> Projeto Inove API </h1>

<p align="center">
<a href="#-prévia">Prévia</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-objetivo">Objetivo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#️-instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-commands">Importação Json</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-dbeaver">Banco de Dados</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-swagger--django-rest-framework---drf--thunder-client">Endpoints</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-conclusão">Conclusão</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-autor">Autor</a>
</p>

<div align="center">

<img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/pedro-hnrq/Proj_ReddFlow" />


</div>



### 📷 Prévia



### 🎯 Objetivo

<h5 align="justify">O Projeto Inove API, é um desafio cujo objetivo é criar uma aplicação web em Python/Django que se comunica com a API  <a href="https://jsonplaceholder.typicode.com/">{JSON} Placeholder</a>  para realizar operações CRUD em posts e usuários. A aplicação permite listar, criar, atualizar e excluir posts, além de listar usuários. Além disso, os dados obtidos da API são armazenados e manipulados em um banco de dados PostgreSQL, implementando operações CRUD completas para os dados armazenados..</h5>


### 🚀 Como executar 

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 
- Django 
- Django REST Framework
- GIT 
- PostgreSQL
- Docker
- Docker Compose


#### 🛠️ Instalação

Os comandos a baixo é para usuário do `Unix` ou no `MacOS`.

🦑 Faça o clone do projeto:

```
git clone git@github.com:pedro-hnrq/Project_Inove.git
```  
Após clonar o repositório acesse o diretório
```
cd Project_Inove
``` 

execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (**Lembre-se de modificá-los**)

```bash
mv env .env
```

#### 🎟️ Ambiente Virtual
Criar Virtualização
```python
python -m venv .venv
```

Ativar o projeto.

```python
source .venv/bin/activate
```
Instalar as dependências
```python
pip install -r requirements.txt
```


Na primeira vez é necessário executar esse comando para aplicar as migrações do banco de dados
```python
python manage.py migrate
```

Criando super usuário para acessar o painel administrativo
```python
python manage.py createsuperuser
```

Executando o Projeto
```python
python manage.py runserver
```

#### 🐋 DOCKER


Antes de tudo, construa e execute o contêiner Docker:


```bash
docker compose up --build
```

Carregando as `migrates` e `runserver`, acesse:

Após iniciar o contêiner, aplique as migrações no banco de dados PostgreSQL:
```bash
docker compose exec app python manage.py migrate
```

**Acesso ao Site e Painel Administrativo**

Para acessar no site e no painel administrativo, crie um superusuário com o seguinte comando:
```bash
docker compose exec app python manage.py createsuperuser
```
```bash
docker compose exec app python manage.py runserver
```

Para iniciar novamente:
```bash
docker compose up -d
```
 Iniciar somente o Banco de Dados:

```bash
docker compose up -d db
```

Obs.: Para que o contêiner PostgreSQL funcione juntamente com sua máquina local, poderá ajustar a configuração no arquivo `.env`. Altere o valor da variável `DB_POSTGRES_HOST` para _localhost_. Isso permitirá que o contêiner do banco de dados seja iniciado com o comando acima. Após inicializar o contêiner, você pode rodar o projeto na sua máquina local, utilizando a configuração ajustada.

Para poder **Parar** a aplicação no docker basta executar
```bash
docker compose down
```

#### 🌐 Commands

Para puxar todas informações Json do site [{JSON} Placeholder](https://jsonplaceholder.typicode.com/) o Post e User, utilize o comando: 

- Para capturar todas informações:

```
python manage.py import_json
```

- Seleciona a quantidade de informação:

```
python manage.py import_json --users 5 
```

#### 🦫 Dbeaver

Para visualizar as as tabelas no banco de dados, poderá usar o `DBeaver Communty`, com as seguintes configurações: 

- Host: localhost
- Port: 5432
- Banco de dados: inove
- Nome de usuário: dev
- Senha: dev@pg

#### 👨🏻‍🚀 Swagger | Django REST Framework - DRF | Thunder Client

Acesse os endpoints da API:

- Swagger e Redoc:
  - localhost:8000/api/swagger
  - localhost:8000/api/redoc

- DRF(Estando logando conseguer realizar as requisições):
  - localhost:8000/api/users
  - localhost:8000/api/users/7
  - localhost:8000/api/posts/41

- Thunder Client (Tem que ter o Token para realizar os requisiçãos endpoint):
  - PUT: localhost:8000/api/posts/15
  - DELETE: localhost:8000/api/posts/100

Para autenticação via Swagger ou Thunder Client, clique em "Authorize" e insira o token.

#### 📓 Conclusão

<h5 align="justify">O Projeto Inove API integra uma aplicação Django REST Framework com uma API externa, realizando operações CRUD em posts e usuários e armazenando dados em um banco de dados PostgreSQL. </h5>


### 💡 Autor 
#### Pedro Henrique Soares Feitosa

## Licença
[MIT License](LICENSE)
