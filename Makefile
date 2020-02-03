test:
	python -m unittest


clean-dist:
	rm -rf dist

dist: clean-dist
	python setup.py sdist

upload-dist:
	twine upload dist/*

upload-dist-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

