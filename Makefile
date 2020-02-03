test:
	python -m unittest

dist:
	python setup.py sdist

upload-dist:
	twine upload dist/*
