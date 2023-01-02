all: install

install:
	python3.10 -m venv venv
	venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python3.10 main.py

tests:
	./venv/bin/python3.10 -m pytest ./tests


docs:
	make docs -c