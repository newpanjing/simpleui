#!/usr/bin/env bash
rm -rf dist/*
python3 setup.py sdist
twine upload dist/*