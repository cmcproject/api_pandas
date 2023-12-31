build:
	docker-compose build

up:
	docker-compose up

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

lock:
	docker-compose run --rm app sh -c "poetry lock"