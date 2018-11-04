publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg trav.egg-info

test:
	python -m pytest
	python -m tests.vars
