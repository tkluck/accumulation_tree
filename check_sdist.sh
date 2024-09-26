#!/bin/bash
set -e
set -o pipefail

make

ROOT="$(pwd)"
TEMPDIR="$(mktemp -d)"

cp -t "$TEMPDIR" dist/*.tar.gz
cd "$TEMPDIR"
tar -xf *.tar.gz
rm *.tar.gz
cd accumulation_tree-*

virtualenv env
env/bin/pip install cloudpickle build
env/bin/python -m build
env/bin/pip install .

cd env
bin/python -m doctest "$ROOT/tests.md" "$ROOT/README.md"
bin/python -Werr -c'import accumulation_tree'
