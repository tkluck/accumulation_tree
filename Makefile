PYTHON ?= python

all:
	$(PYTHON) setup.py install

env:
	virtualenv -p $(PYTHON) env

check: env
	env/bin/python setup.py install
	env/bin/pip install cloudpickle
	(cd env && bin/python -m doctest ../tests.md ../README.md) # don't have pwd equal to toplevel or it will load (uncompiled) packages from there

check_sdist: env
	./check_sdist.sh

clean:
	rm -rf env build accumulation_tree.egg-info dist

release: clean env
	env/bin/python setup.py build sdist --formats gztar
	twine upload dist/*.tar.gz
