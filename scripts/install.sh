#!/bin/bash
cd /home/ec2-user/myproject
source /home/ec2-user/venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
deactivate