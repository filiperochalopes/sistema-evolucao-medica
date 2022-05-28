# O que é um MAPA?

MAPA de pacientes é uma ferramenta onde colocamos de forma resumida os dados relevantes dos paciente internados para melhorar o seguimento do cuidado.

# Sobre o sistema

O sistema foi criado para viabilizar um mapa simples, como um projeto piloto pessoal para minha prática médiga em uma Policlínica 

### Gerando secret key

```sh
python -c 'import secrets; print(secrets.token_hex())'
```

```
docker-compose up
```

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```