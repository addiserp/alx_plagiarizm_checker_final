#!/usr/bin/env bash



tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 main:app'
tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
