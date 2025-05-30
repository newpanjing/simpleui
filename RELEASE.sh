#!/usr/bin/env zsh
echo 'delete cache'
rm -rf simpleui/templatetags/__pycache__
echo 'release django-simpleui...'
rm -rf dist/*
python3 setup.py sdist
twine upload dist/*

echo 'release django-simpleui success.'

echo 'release simpleui...'
rm -rf dist/*
python3 setup2.py sdist
twine upload dist/*

echo 'release simpleui success.'