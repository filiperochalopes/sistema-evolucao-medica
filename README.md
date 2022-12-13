# Sistema de Evolução Clínica

Inicialmente criado com a ideia de ser um registro para acompanhamento de pacientes por médicos de um pronto atendimento, o conceito foi migrado ao notar a debilidade de um Hospital de Pequeno Porte em registrar as condutas de seus pacientes. Esse novo escopo visa ser responsável pela melhoria da comunicação e atenção da equipe.

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
cd flaskapp/app/templates/reactapp
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

# Como rodar os testes
### Entre no diretorio /app/app
```cd /app/app```
### Agora rode os teste utilizando esse comando
```pytest /app/app/tests/pdfs/```

### O resultado é pra ser parecido isso:
```
root@d956c3253006:/app/app# pytest /app/app/tests/pdfs/
========================================================================================== test session starts ==========================================================================================platform linux -- Python 3.8.15, pytest-7.1.3, pluggy-1.0.0
rootdir: /app/app
plugins: anyio-3.6.1
collected 819 items
```