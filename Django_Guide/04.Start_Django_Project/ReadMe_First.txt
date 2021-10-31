Using Terminal/CMD/Command Prompt/Powershell

1. Create django project

>> django-admin startproject anyname . 
     (0n anyname -> put anyname like my MyPro, MyWeb, MyDev ..will do)
**** Put space and the a dot(.) after anyname

anyname Folder will appear and manage.py File

2 Run django server/Web

>> python manage.py runserver

db.sqlite shold apprear

(These link "http://127.0.0.1:8000/" should appear, then copy the link to your browser/ click the link will direct you to default browser)

*** Do not close the terminal, server will stop running if close.

3. To clear the Red error run migration on the terminal as it point out "Run 'python manage.py migrate' to apply them."

>> python manage.py migrate
