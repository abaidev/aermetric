echo "Collect static files"
python3 /code/manage.py collectstatic --noinput

echo "Apply database migrations"
python3 /code/manage.py migrate

echo "DJANGO SERVER starts"
python3 /code/manage.py runserver 0.0.0.0:8000
