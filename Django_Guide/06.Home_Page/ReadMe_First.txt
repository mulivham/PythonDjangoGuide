Using IDE/Text Editor (eg.Vs Code, Subline)

1. Edit Views.py File

Go to views.py File inside Page Folder/ App Folder you created

(You need to import HttpResponse )
Copy and paste/ Type the follow :

from django.http import HttpResponse

(Next few line)
Create your own view like :

def HomeView(request):
    return HttpResponse('Welcome To My Home')

** Note ( HomeView = is a Fuction i have given, you can give it anyname as long as it is not long, untidy, u can use the name like : "home_view", "ViewOfHome" or just simple "Home" "index", just make sure you keep in mind, cause it will be used in other file the way u named it )

2. EDIT urls.py FILE

Go to urls.py File inside your project Folder (in my case inside MyWeb, Folder folder contain settings)

(You need to import views file from Page Folder/ whatever in your incase)
Copy and paste/ Type the follow :

from Page import views

Add a new path next to a default :

path('', views.HomeView),

***Remember ( "Page", and HomeView are being used now, if you get an error, check your spelling, other characters are the same way you given them)

After all that make sure save all file, if your server is still running on your terminal, click/ copy and paste the link in your browser.

Browser should display the string you wrote on function inside the view.py file
Result:

Welcome To My Home

*** If succesfull, Weldone, You hace Create the Home page, Move to next Step.

*** If unsuccessful, got back fews step and check if everyting is correct, spelling, funny character and finally check what the terminal says, it will point out the problem

run the server in if is off:

python manage.py runserver





