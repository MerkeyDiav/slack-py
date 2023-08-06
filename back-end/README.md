Liste des commandes à utiliser avant de lancer le serveur Django

**installer l'environnement**
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install .\requirements.txt
py .\manage.py makemigrations
py .\manage.py migrate
py .\manage.py runserver
