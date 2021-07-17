#!/bin/sh
# also may want to use '-b 0.0.0.0:80'
# sudo gunicorn --chdir main main:main -w 2 --threads 2

sudo python main.py