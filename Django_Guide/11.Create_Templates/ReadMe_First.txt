Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) 

Python(.py) script/file to use : settings.py , views.py

1. Templates

Create templates folder where you will save html Script/Files (see screenshot 01.Create_Temp_Folder )

Create html Script/Files inside Template folder (see screenshot 02.Html_Files)

Write Html codes inside html file( home.html) 

You may need to study html codes, to get a better understanding, which it may took too much time.

for now, use html code, like 
	eg: <h1> message inside </h1>
	(see screenshot 03.Html_Codes) & html file inside template folder
	

2. Edit Views.py Script/File

Replace >> 

return HttpResponse('<h1>Welcome To My Home</h1>')

with >>

return render(request,'home.html', {})

** Note : where there is home.html you replace it the one you have created

(see screenshot 04.Edit_Views)

3. Edit Setting.py script/File

step 1 : On the setting.py file, you need to add :

import os

(os means operating system)

see screenshot 05.Add_Import

Step 2 : 

add : 'DIRS': [os.path.join(BASE_DIR,"Templates")] inside where they written TEMPLATES

** Note : The above steps may not needed on the latest django version, and may not work on the django version, if you encounter such problem you need to read the hashtag(#)/commented instructions above on setting.py file which came with links to lead you to a better understanding of what you may need to do in this python file(settings.py)

(see screenshot 06.Edit_Setting)

4. Make sure You saved all files , and run the server on the terminal and see the result on the browser

(see screenshot 07.Home_Page)
















