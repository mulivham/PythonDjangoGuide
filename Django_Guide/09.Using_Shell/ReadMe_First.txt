Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) 

1. Activate Shell

on the terminal type :

python manage.py shell

2. Adding Fields

On the terminal type :

from Page.models import Page

To Add or Create Content:

Page.objects.create(title='Article on Shell', content='This is written on shell')

To Check Numbers of Content :

Page.objects.all()

to exit : >> exit()

3. Check Browser

Run the server if not running, Use your browser to login via /admin page and you will see more numbers o objects added




