seed:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash -c "FLASK_APP=app/__init__.py && \
	flask seed"
terminal:
	docker exec -it mapa_ga_filipelopesmedbr_flaskapp bash