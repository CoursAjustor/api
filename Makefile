init:
	pip install -r requirements.txt
	rm database/data/courses.db
	touch database/data/courses.db
	python3 init.py

start:
	export FLASK_APP=app.py
	flask run