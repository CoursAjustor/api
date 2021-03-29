init:
	pip install -r requirements.txt

start:
	export FLASK_APP=app.py
	flask run