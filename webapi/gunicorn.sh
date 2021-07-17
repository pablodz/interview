#!/bin/sh
# also may want to use '-b 0.0.0.0:80'
gunicorn --chdir main main:main -w 2 --threads 2