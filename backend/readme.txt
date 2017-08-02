How to run backend:
1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python manage.py makemigrations rest_api
5. python manage.py migrate
6. python manage.py runserver
