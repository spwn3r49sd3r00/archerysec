# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

#!/bin/bash

python manage.py collectstatic --noinput

# wait for Postgres to be available
if [ -z "$DB_HOST" ]
then
    echo "not running posgres"
else
  until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
  done

  >&2 echo "Postgres is up - executing migrations"
  exec $cmd
fi

python manage.py migrate sitetree --noinput
python manage.py migrate --noinput
python manage.py initadmin

if [ "$ARCHERY_WORKER" = "True" ]
then
    python manage.py process_tasks
else
    python manage.py sitetree_resync_apps
    python manage.py runserver 0.0.0.0:8000
fi
