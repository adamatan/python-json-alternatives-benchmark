#!/bin/bash

# exit when any command fails
set -e

# Echo the executed commands
set -o xtrace

mypy  --ignore-missing-imports --disallow-untyped-defs src
black --check src
pylint --rcfile=pylintrc src
