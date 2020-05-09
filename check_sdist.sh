#!/bin/bash
set -e
set -o pipefail

ROOT="$(pwd)"
TEMPDIR="$(mktemp -d)"

env/bin/python setup.py build sdist -d "$TEMPDIR" --formats gztar

cd "$TEMPDIR"
tar -xf *.tar.gz
rm *.tar.gz
cd accumulation_tree-*

virtualenv env
env/bin/python setup.py install
env/bin/pip install cloudpickle

cd env
bin/python -m doctest "$ROOT/tests.md" "$ROOT/README.md"
bin/python -Werr -c'import accumulation_tree'
