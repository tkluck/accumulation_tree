PYTHON ?= python

all:
	$(PYTHON) setup.py install

env:
	virtualenv -p $(PYTHON) env

check: env
	env/bin/python setup.py install
	env/bin/pip install cloudpickle
	(cd env && bin/python -m doctest ../tests.md)

clean:
	rm -rf env build accumulation_tree.egg-info dist
