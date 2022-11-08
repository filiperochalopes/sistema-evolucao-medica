build:
	docker-compose build --no-cache
run:
	docker-compose up --build
logs:
	docker-compose logs -f
seed:
	docker exec -it evolucao_hospitalar_flaskapp bash -c "FLASK_APP=app/__init__.py && \
	flask seed"
terminal:
	docker exec -it evolucao_hospitalar_flaskapp bash
shell:
	docker exec -it evolucao_hospitalar_flaskapp bash -c "flask shell"
migrate:
	docker exec -it evolucao_hospitalar_flaskapp bash -c "flask db upgrade"
makemigrations:
	docker exec -it evolucao_hospitalar_flaskapp bash -c 'flask db migrate -m "$(m)"'
reset_db:
	docker exec -it evolucao_hospitalar_flaskapp bash -c ' \
		rm -rf migrations && \
		rm -rf instance && \
		flask db init && \
		flask db migrate -m "Initial migration" && \
		flask db upgrade'