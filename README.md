# Sistema de Evolução Clínica

Inicialmente criado com a ideia de ser um registro para acompanhamento de pacientes por médicos de um pronto atendimento, o conceito foi migrado ao notar a debilidade de um Hospital de Pequeno Porte em registrar as condutas de seus pacientes. Esse novo escopo visa ser responsável pela melhoria da comunicação e atenção da equipe.

## Deploy em ambiente de homologação/produção

1. (Opcional) Crie dentro da pasta app uma lista de usuários para cadastro/seed inicial
2. Execute:

```sh
docker-compose down --volumes --remove-orphans
rm -rf data
docker-compose up -d
make migrate
make seed
make users
```

## Ambiente de desenvolvimento

Para desenvolvimento foi criado um ambiente docker que supre as necessidades da construção, entretando para produção será instalado em um computador Windows de baixo custo da unidade que funcionará como servidor.

### Gerando secret key

```sh
python -c 'import secrets; print(secrets.token_hex())'
```

```
docker-compose up
```

## Reset app

```sh
make run
make migrate
```

## Comandos de migrations

```sh
make migrate
make m="update some table" makemigrations
```

## Utilizando o alembic no ambiente de desenvolvimento

```sh
# Abrindo terminal no container flask
make terminal
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Ambiente de produção

Orientações para instalação de todo o sistema em Windows

### instalando dependências

Instalamos o [python](https://www.python.org/downloads/) e o [node](https://nodejs.org/en/download/). Após isso ié necessário [criar um ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html#creating-virtual-environments) e o [yarn] que será necessário para criar a build React:

```sh
npm install --global yarn
```

### Realizando a build React

```sh
cd reactapp
yarn
yarn build
```

### Rodando aplicação completa

```sh
cd flaskapp
# criando ambiente virtual
python -m venv path/to/myenv
# ativando o ambiente virtual
myenv/Scripts/activate
FLASK_APP=app/__init__.py
FLASK_DEBUG=false
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon
```

### Rodando ao inicializar Windows 7

Salvar arquivo `C:\Users\(username)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\run_internment.bat`:

```bat
@echo off
cd C:\path\to\project
myenv/Scripts/activate
FLASK_APP=app/__init__.py
FLASK_DEBUG=false
gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon
```

### Testes

Para facilitar o teste estou mantendo no README algumas requisições para preencher o banco de dados com informações iniciais e úteis para o teste estão disponíveis na lista de comando do `Makefile`
