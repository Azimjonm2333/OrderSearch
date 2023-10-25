runserver:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

collect:
	python3 manage.py makemigrations
	python3 manage.py migrate
