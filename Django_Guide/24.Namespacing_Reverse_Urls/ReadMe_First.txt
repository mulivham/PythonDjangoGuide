Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) 

** NOTE : THIS STEP IS OPTIONAL

Script/File to use : Urls.py>, Models.py>
Script/File to create : Urls.py>

1. Create a urls python script inside page app/folder (see screenshot 01.Create_Urls_File)

2. Move similar related path or path that belong to a specific app to the new urls.py file from the main urls.py file, make your you add "include" next tp path import and all the new urls path "path('blog/', include('blog.urls'))" for an example. (see screenshot 02.Edit_Urls)

3. add a Namespace (app_name) on the new urls script before the urls patterns (see screenshot 03.Edit_New_Urls)

***Note : Namespacing and naming your makes it easier for django to find the path and use it as a shortcuts and also to simply use it on the reverse urls on model.py (screenshot 04.Edit_Model)to make it more dynamic

You may also need to remove the the first forward slash on each path to avoid an error (screenshot 05.Page_Error)

4. Add Namespace (app_name) on the reverse function in the model.py file/script and also add your id (screenshot 04.Edit_Model)

5 You may still enconter some error after saving, if you do, check if the everythings is redirected / updated to the right path or urls, since there have been some changes on the urls patterns and urls.py files 
(screenshot 06.Redirect_Changed) (screenshot 07.HTML_Link)


