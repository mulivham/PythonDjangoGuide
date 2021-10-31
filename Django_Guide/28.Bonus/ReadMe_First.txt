Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) 


1.Login/ Logout

By using build in logins code, we need to import login/ logout views from  django.contrib.auth.views (see screenshot 01.Login_logout_urls), which is located on our virtual environment (see screenshot 02.Auth_Views_Path)

When trying to login, your will see template error, indicating the absent of a login template (see screenshot 03.Template_Error), so we need to create an template sub-folder and file (see screenshot 04.Template_SubFolder) & (see screenshot 05.HTML_Login), according to the Views.py file (see screenshot 06.Auth_Views) from the virtual environment path (see screenshot 02.Auth_Views_Path), when done and saving all files, you will be able to see login page (see screenshot 07.Login_Browser)

**Note : enviroment Path = env/lib/python3.7/site-packages/django/contrib/auth/views.py

2. Signup/  Resgister

Will have to create signup/register views (see screenshot 08.Signup_Views) by import UserCreationForm forms from  django.contrib.auth.forms (see screenshot 09.User_Creation_Form), which is located on our virtual environment (see screenshot 10.Auth_Forms_Path)

Create a signup path/ urls patterns after importing Signup views (see screenshot 11.Signup_Urls) and create signup template in same folder with login, when done , should be able to see signup page on the browser (see screenshot 12.Signup_Browser)

Rediect/ return your succefull url to home page("/") on your signup views to avoid Browser error (see screenshot 13.Reverse_Urls) due to unknown urls (see screenshot 14.Unknown_Urls)

You may encounter some error when login in, loging out and signing up,(see screenshot 15.Wrong_Urls1), (see screenshot 16.Wrong_Urls2), because build in django will redirect to unknown urls, so we need to add our urls on the settings.py file (see screenshot 17.Settings_Urls) so that when everything went well, it should redirect to me page or somewhere to avoid those errors

Now you should be able to register/ signup (see screenshot 18.Succefull_Signup), information will be store on the database and it should be visible on the admin page (see screenshot 19.Admin_User)

#OPTION 2 : SIGNUP

Create your own custom form inside forms.py (see screenshot 20.Custom_Forms) and change your Signup View by import forms to views (see screenshot 21.Custom_Signup_Views)


3. Login Required Mixin

Put an mixin argument inside the class fuction of your choise, or a page that required to login first before using it. (in my case is createview and listview), (see screenshot 22.Mixin) , when trying to access a page with mixin it with redirect to unknown urls (see screenshot 23.Unknown_Mixin_Urls), so we need to redirect it to logn in page when mixin is required by adding more setting (see screenshot 24.Settings_Urls2)

4. Base/ Navbar template/Html

Put an (if statement ) on the base or navbar template (see screenshot 25.HTML_Template1) & (see screenshot 26.HTML_Template2), to make work according to your mixins, When logout you wont be able to see the list and to create the post, and if statement makes it possible for template to hide some feature when not logged in.
(see screenshot 27.Browser_Logged_out) & (see screenshot 28.Browser_Logged_in)

**Note : Try login after you have logged out



