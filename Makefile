all: main.py
	python main.py test.smin

debug: main.py
	python main.py test.smin -d
