import os, shutil

# finding the folder path
Path = '/Users/joshuadizon/Downloads'

# adding all the files to a list
files = os.listdir(Path)

# go through every file in the download folder and creates a new variable called file
for file in sorted(files):

	# splits the file name and the file extention, name of the file wont be used
	name, extension = os.path.splitext(file)

	# removes the '.' form the extension
	extension = extension.replace('.','')

	# Gets rid of any extention bugs	 
	if extension == '':
		continue
	
	# statement to see if theres a folder with the same name as the extention and if its true then move to it.
	if os.path.exists(Path + '/' + extension):
		shutil.move(Path +'/'+ file, Path + '/' + extension + '/' + file)
		
	# if theres not folder then create one and move the file to corresponding folder with the same extention
	else:
		os.makedirs(Path + '/' + extension)
		shutil.move(Path + '/' + file, Path + '/' + extension + '/' + file)


























