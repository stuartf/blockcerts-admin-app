#!/bin/bash

python3 /code/manage.py migrate --noinput
python3 /code/push_cert_tools_config.py
python3 /code/manage.py runserver 0.0.0.0:8000
