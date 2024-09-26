PYTHON ?= python3

all:
	$(PYTHON) -m build

env:
	virtualenv -p $(PYTHON) env
	env/bin/pip install build cloudpickle

check: env
	env/bin/python -m build
	env/bin/pip install .
	(cd env && bin/python -m doctest ../tests.md ../README.md) # don't have pwd equal to toplevel or it will load (uncompiled) packages from there

check_sdist: env
	./check_sdist.sh

clean:
	rm -rf env build accumulation_tree.egg-info dist

release: clean all
	twine upload dist/*.tar.gz dist/*.whl
