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
	docker exec -it evolucao_hospitalar_flaskapp bash -c ' \
		chmod -R 777 /app/migrations/versions && \
		flask db upgrade'
makemigrations:
	docker exec -it evolucao_hospitalar_flaskapp bash -c ' \
		chmod -R 777 /app/migrations/versions && \
		flask db migrate -m "$(m)"'
test:
	docker exec -it evolucao_hospitalar_flaskapp bash -c 'pytest -s'
reset_db:
	docker exec -it evolucao_hospitalar_flaskapp bash -c ' \
		rm -rf migrations && \
		rm -rf instance && \
		flask db init && \
		flask db migrate -m "Initial migration" && \
		chmod -R 777 /app/migrations/versions && \
		flask db upgrade'