PYTHON ?= python3

all:
	$(PYTHON) -m build

env:
	virtualenv -p $(PYTHON) env
	env/bin/pip install build cloudpickle

check: env
	env/bin/python -m build
	env/bin/pip install .
	env/bin/python -m doctest tests.md README.md

check_sdist: env
	./check_sdist.sh

clean:
	rm -f src/accumulation_tree/accumulation_tree.c
	rm -rf env build src/accumulation_tree.egg-info dist

release: clean all
	twine upload dist/*.tar.gz dist/*.whl
