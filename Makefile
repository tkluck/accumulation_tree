all:
	python setup.py install

env:
	virtualenv env

check: env
	env/bin/python setup.py install
	env/bin/python -m doctest tests.md
