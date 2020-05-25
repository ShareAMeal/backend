# Backend Django

Pour démarrer: installer les dépendances:
```
pip3 install --user -r requirements.txt
./manage.py migrate # initialise la base de données
./manage.py runserver # lance le serveur
```

## Traductions
Après un changement du code:
```shell script
cd api && ../manage.py makemessages -l fr
cd api && ../manage.py makemessages -l en
cd api && ../manage.py compilemessages

cd register && ../manage.py makemessages -l fr
cd register && ../manage.py makemessages -l en
cd register && ../manage.py compilemessages
```