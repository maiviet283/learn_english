#!/usr/bin/env bash
set -o errexit

# Web không dùng database nên không cần migrate/loaddata.
# gthread: mỗi worker có nhiều luồng để vừa phục vụ trang vừa tạo âm thanh (edge-tts) song song.
exec gunicorn english.wsgi:application --workers 2 --threads 8 --timeout 60
