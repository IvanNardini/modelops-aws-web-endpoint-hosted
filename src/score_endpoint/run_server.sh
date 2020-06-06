#!/bin/sh

exec gunicorn --bind 0.0.0.0:9999 wsgi:app \
    --log-level=debug \
    --log-file=/var/log/gunicorn.log \
    --access-logfile=/var/log/gunicorn-access.log \
"$@"
