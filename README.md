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

### Testes

Para facilitar o teste estou mantendo no README algumas requisições para preencher o banco de dados com informações iniciais e úteis para o teste

```graphql
mutation{
  signin(email:"contato@filipelopes.med.br", password:"passw@rd"){
    user{
      id
      name
      birthdate
    }
    token
  }
}
```

```graphql
mutation {
  createInternment(
    admissionDatetime: "2022-11-21 15:22"
    patient: {
    name:"Orlando Flórida"
    sex:"male"
    birthdate:"1995-12-01"
    cns: "105118227480000"
    cpf: "33131763990"
    weightKg: 65.5
    comorbidities: ["Hipertensão Arterial Sistêmica (HAS)", "Diabetes Mellitus (DM)"]
    allergies: ["Dipirona", "Amoxicilina", "latex"]
    address: {
      street:"Rua Orlando Flórida"
      zipCode:"40440360"
      complement: ""
      city:"Água Fria"
      uf: "BA"
    }
  },
  	hpi: "lorem ipsum"
    justification: "lorem ipsum"
    cid10Code: "I11"
  ){
    id
    hpi
    patient{
      id
      name
      cns
    }
  }
}
```

```graphql
mutation {
  createEvolution(
    internmentId: 1,
    text: "Lorem ipsum"
    prescription: {
      restingActivity: "Repouso relativo"
      diet: "Dieta Zero"
      drugs: [{
        drugName: "Nome da medicação"
        drugKind: "oth"
        dosage: "1 comprimido 6/6h"
        route: "Via Oral"
      }, {
        drugName: "Antibiótico"
        drugKind: "atb"
        dosage: "1 ampola 12/12h"
        route: "Via Venosa"
        initialDate: "2022-11-13 22:10:20"
        endingDate: "2022-11-20 22:10:20"
      }]
      nursingActivities: ["Sinais vitais 6/6h"]
    }
    pendings: "Aqui vão as pendências"
    cid10Code: "I20"
  ){
    evolution{
      id text createdAt
    }
    prescription{
      restingActivity{
				name
      }
      diet{
        name
      }
      drugPrescriptions{
        drug{
          name
        }
        dosage
      }
      nursingActivities{
        name
      }
      createdAt
    }
    pendings{
      text
    }
  }
}
```