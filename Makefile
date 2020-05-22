install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C predictor.py
run:
	python main.py, predictor.py
