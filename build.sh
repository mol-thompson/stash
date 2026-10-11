#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install production dependencies
pip install uv
uv sync --no-dev

# Convert static asset files
.venv/bin/python manage.py collectstatic --noinput

# Apply any outstanding database migrations
.venv/bin/python manage.py migrate
