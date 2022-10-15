#!/bin/sh
cd /app
gunicorn 'main:app' -b 0.0.0.0:8080