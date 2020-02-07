import os, shutil

# Folder path
Path = '/Users/joshuadizon/Downloads'

# Creating a list of all files
files = os.listdir(Path)

# Creates a variable for every single file within Downloads.
for file in sorted(files):

	# Splits file name from file extension
	name, extension = os.path.splitext(file)

	# Removes "." (period) from the file name and replaces it with a [space].
	extension = extension.replace('.','')

	# Rids of extension bugs (human error)	 
	if extension == '':
		continue
	
	# Checks if there is a folder with the existing file extension.
	if os.path.exists(Path + '/' + extension):
		shutil.move(Path +'/'+ file, Path + '/' + extension + '/' + file)
		
	# If there is no folder with the same file extension, it creates a new one for the brand new file extension found.
	else:
		os.makedirs(Path + '/' + extension)
		shutil.move(Path + '/' + file, Path + '/' + extension + '/' + file)


























