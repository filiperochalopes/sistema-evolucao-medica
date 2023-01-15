build:
	docker-compose build --no-cache
run:
	docker compose up --build
logs:
	docker compose logs -f
seed:
	docker exec -it evolucao_hospitalar_app bash -c "FLASK_APP=app/__init__.py && \
	flask seed"
terminal:
	docker exec -it evolucao_hospitalar_app bash
shell:
	docker exec -it evolucao_hospitalar_app bash -c "flask shell"
migrate:
	docker exec -it evolucao_hospitalar_app bash -c ' \
		chmod -R 777 /app/migrations && \
		flask db upgrade'
makemigrations:
	docker exec -it evolucao_hospitalar_app bash -c ' \
		chmod -R 777 /app/migrations && \
		flask db migrate -m "$(m)"'
test:
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s'
clean_db:
	docker compose rm -s -v -f db
	sudo rm -rf data
	docker compose up -d db
	docker exec -it evolucao_hospitalar_app bash -c ' \
		rm -rf instance && \
		flask db upgrade'
fix-folder-permission:
	docker exec -it evolucao_hospitalar_app bash -c ' \
		chmod -R 777 /app/migrations'