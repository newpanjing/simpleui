#!/usr/bin/env bash
echo 'release django-simpleui'
rm -rf dist/*
python3 setup.py sdist
twine upload dist/*
echo 'django-simpleui upload success!'

echo 'release simpleui'
python3 setup2.py sdist
twine upload dist/*
echo 'simpleui upload success!'