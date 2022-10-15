#!/bin/sh
gunicorn --chdir app viscon_hackathon_2022:app -w 4 -b 0.0.0.0:8080