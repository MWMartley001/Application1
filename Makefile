install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C main.py
run:
	python main.py