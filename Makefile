run:
	docker-compose up -d --build
logs:
	docker-compose logs -f
seed:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash -c "FLASK_APP=app/__init__.py && \
	flask seed"
terminal:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash
migrate:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash -c "flask db upgrade"
makemigrations:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash -c 'flask db migrate -m "$(comment)"'