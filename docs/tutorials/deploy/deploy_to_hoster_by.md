`deploy to hoster.by`
=

1. Create django app in cPanel, add project path, set python version
2. activate virtual env and go to the project folder
3. git clone repository
4. set public folder to project, public --> manage.py...
5. pip install -r requirements.txt
6. set passenger wsgi to 
```
import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/public') 

os.environ['DJANGO_SETTINGS_MODULE'] = "ENGINE.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 
```
7. change settings.py : add database 'OPTIONS': {'sql_mode': 'traditional'},
8. collectstatic
9. migrate
