Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) 

Script/File to create : forms.py , Sub Template Folder, html file.
Script/File to use : views.py 

1. Create

> Create python script/file called forms.py inside your app folder(Page)
(see screenshot 01.Create_Form)

> Create Folder inside a Template Folder(give any anyname) (in my case the folder is called : Form)

> create Html script/file inside the sub folder you created inside template folder(in mycase : create_post.html)

2 Edit & Code

> Code forms.py file and save (screenshot 02.Forms.py)

> Edit views.py file and save ( see screenshot 03.Views.py)

> code the html file/script with the following codes (see screenshot 04.Html)

> Edit urls.py file/Script to add a new path for a html template (see screenshot 05.Edit_Urls)

3. Browser

> Navigate your bowser to a newly created path (in mycase is : 000/create/) created on urls.py (see screenshot 05.Edit_Urls), (see screenshot 06.Browser_Form) for the result

> You can write some messages (see screenshot 07.Write_Message) and save/send, your message will be save on the database and appear on the admim page (see screenshot 08.Database_Browser)

> open up the latest/last data message (in mycase : Page object (4) ) on the admin page (see screenshot 09.View_Object), you will the message you just wrote, message can be edited and deleted as a superuser/admin.

> Since the last message is marked as {Page object (4)}, where 4 is an id number, you need to change an id number at views.py from 1 to 4 (see screenshot 10.Id_No) in order to display your message on the page(community page) (see screenshot 11.Posted_Message)



