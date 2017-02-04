all:
	python setup.py install

env:
	virtualenv env
	env/bin/pip install -r requirements.txt

check: env
	env/bin/python setup.py install
	env/bin/python -m doctest tests.md
