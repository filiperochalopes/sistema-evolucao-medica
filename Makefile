build:
	docker-compose build --no-cache
run:
	docker compose up --build
logs:
	docker compose logs -f
seed:
	docker exec -it evolucao_hospitalar_app bash -c "FLASK_APP=app/__init__.py && \
	flask seed"
users:
	docker exec -it evolucao_hospitalar_app bash -c "FLASK_APP=app/__init__.py && \
	flask create_users"
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
test_all:
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s'
clean_db:
	docker compose rm -s -v -f db
	sudo rm -rf data
	docker compose up -d db
	sleep 10
	docker exec -it evolucao_hospitalar_app bash -c ' \
		flask db upgrade'
test_flow:
	# Clean all database
	docker exec -it evolucao_hospitalar_db bash -c 'psql -U postgres -c "\set AUTOCOMMIT on" -c "DROP DATABASE hmlem WITH (FORCE)" -c "CREATE DATABASE hmlem"'
	docker exec -it evolucao_hospitalar_app bash -c 'flask db upgrade && flask seed'
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s -k TestInternmentFlow'
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s -k TestPrintPdfs'
test_pdfs:
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s -k test_evol_compact'
	docker exec -it evolucao_hospitalar_app bash -c 'pytest -s -k test_apac'
fix-folder-permission:
	docker exec -it evolucao_hospitalar_app bash -c ' \
		chmod -R 777 /app/migrations'