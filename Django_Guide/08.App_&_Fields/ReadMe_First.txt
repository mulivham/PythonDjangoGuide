Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) &

Keep in mind : Python File/Script to use are : Setting.py, admin.py & models.py

1 Edit Models.py File

Go to Django official web and look for models, depending on what kind of app you designing. 

for example : Product app may need Price field, Article app may need content field and so on.

(in my case :

class Page(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
)

Check Screenshot 01 for example
 
2. Edit Admin.py File

from .models import Page #(<<copy and paste)

admin.site.register(Page) #(<<copy and paste

you need to register your models here or copy and paste, after import your app(Page) from models.py file from as directory, hance(.models)
 
See screenshot 02 for an example

3. Edit Settings.py File

You need to put the name of the app/folder your created inside >> INSTALLED_APPS [ name of the app here]

(In My case its INSTALLED_APPS [Page,] )

Check screenshot 03

4. Make sure you saved all Edited Python (.py) files and run the command on the terminal :

python manage.py makemigrations

python manage.py migrate

( Run those command everytime you make some changes on models.py script/files)

5. Browser Check

Run the server if not running, Use your browser to login via /admin page, inside admin home, Name of App with new File would be visible on the browser 

Check Screenshot for example 