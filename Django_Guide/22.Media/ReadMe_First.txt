Using Terminal/CMD/Command Prompt/Powershell & Browser (Google Chrome, Opera, Fire Fox, explorer and etc) & IDE/Text Editor (eg.Vs Code, Subline) 

Script/File to use : Settings.py>, Urls.py>, Models.py>, Forms.py>, Views.py and Html(on details and create template)

1. Create a folder named Media, a folder which will save uploaded media file like images, music, videos and etc. (see screenshot 01.Create_Folder)

2.Put/type a MEDIA Directory/ Path inside settings.py file (see screenshot 02.Edit_Settings)

3.Import module for media (see screenshot 03.Urls_Module) and add a static path for media (see screenshot 04.Urls_Path)

4.Add image/file field on models.py script (see screenshot 05.FileField) and run makemigrations and migrate on your terminal (see screenshot 06.Terminal)

5. Run the server and your browser to adnin page, note that the file field is added (07.Browser_Admin) and you can upload any file you like, any file that is uploaded will be saved on the Files Sub-Folder of Media Folder (see screenshot 08.Files_Folder)

6. You may wanna Add/ Change Fields (see screenshot 09.Change_Field), Some Fields works perfectly fine with the help of python libraries, e.g python library for images, "pillow" which can handle large and different types/format of images.  
To install libraries you need to install pip first if you dont have one, then type the command : pip install pillow ( or any library you want), run makemigration and migrate for the changes you made (see screenshot 10.Terminal_2)

7. Add a page field on the forms.py script (see screenshot 11.Edit_Forms) for the field to be visible or appear on the your create page (see screenshot 12.Browser_Create)

8. Add Html image codes (see screenshot 13.HTML_Detail)on detail html or where/any html you want to make your uplaoded images to appear or displayed, You may wanna change the format on create html form (see screenshot 14.HTML_Create)

9. Edit the Views.py script on the create post to add codes that will make the form to save the images/file (see screenshot 15.Edit_Views_Create)

10. Makes sure you save all files, create a new post that include the images save it and it will appear on the image sub-folder of files folder and all on your browser (see screenshot 16.Browser_View)

**Note : Your may experience an errors when trying to access previous post (see screenshot 17.Errors), because of the addition/changes in fields, the solution to that for now is to update the post using the admin page or add some code on the update post view line , like we did with create post view (see screenshot 18.Update_Post_View), this will allow your page to be update with a new field on it.(see screenshot 19.Browser_Update)

if you try to view previous pages/post, it will respond (see screenshot 20.Browser_Post) and all images will be save on img sub-folder (see screenshot 21.Image_Sub-Folder )

11. You may like to add image on your home page manually, edit/use the home.html ( see screenshot 22.Edit_HTML_Image ), Selected image will load on home page ( see screenshot 22.Home_Base ), You may wanna Inspect element by clicking left(option) and scrolling down, see how the web was made ( see screenshot 23.Inspect_Element )

12. Updated : insect a "if statement" inside detail html to allow the post without images to display ( see screenshot 24.If_Statement_HTML )
