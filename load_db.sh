klarna-venv/bin/python addressbook/manage.py makemigrations
klarna-venv/bin/python addressbook/manage.py migrate
klarna-venv/bin/python addressbook/import.py data/people.json
klarna-venv/bin/python addressbook/manage.py loaddata addressbook/search/fixtures/people.json

