import os
import shutil
import sys
import platform
import hashlib 
import socket
from subprocess import call
from ntpath import split
from ntpath import basename


#path to scan the top 'n' files of the system and also to find rhe duplicates!
#and delimiter to use!
path_to_scan = ''
delimiter = ''
if platform.system() == 'Windows':
	plat = 'Windows'
	delimiter = '\\'
	path_to_scan = 'C:\\User\\'
else:
	plat = 'Not Windows'
	delimiter = '/'
	path_to_scan = '/home/'

#BONUS
#function to return the public ip of your system
def get_ip():
	return ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#BONUS
#function to create a script to open the HTTP Server
def on_server():
	if plat == 'Windows':
		file_obj  = open('./file.bat', 'w')
	else:
		file_obj  = open('./file.sh', 'w')
	file_obj.write('python -m SimpleHTTPServer 8000')
	file_obj.close()

	if plat == 'Windows':
		call('start /wait file.bat', shell=True)
	else:
		call(['gnome-terminal','-e', 'bash file.sh'])

#function to read the file chunkwise!
def read_chunks(fd):
	while(1):
		chunk = fd.read(1024)
		if not chunk:
			return
		yield chunk

#BONUS
#function to print the duplicate files path!
def print_duplicates():
	#dictionary to keep hashes of file!
	hashed = {}
	#recursively search for folders and check their files sizes!
	for path, subdirs, files in os.walk(path_to_scan):
		#for excluding hidden files and folders!
		files = [f for f in files if not f[0] == '.']
		subdirs[:] = [d for d in subdirs if not d[0] == '.']
		i = 1
		for file in files:
			try:
				hash_obj = hashlib.sha1()
				path_of_file = os.path.join(path, file)
				fd = open(path_of_file,'rb')
				for chunk in read_chunks(fd):
					hash_obj.update(chunk)
				#create file_key using the file content!
				file_key = (hash_obj.digest(), os.path.getsize(path_of_file))
				duplicate = hashed.get(file_key, None)
				if duplicate:
					print i,
					print " "+path_of_file +" and "+ duplicate
					i = i+1
					print 
				else:
					hashed[file_key] = path_of_file
			except OSError:
				#to pass the access denied kinds of files!
				pass

#helper function to sort files according to extensions!
def moveFAEhelper(path,file,ext):
	#to make folder if does not exist!
	path_of_folder = path+ext[1:].upper()
	if not os.path.exists(path_of_folder):
		os.makedirs(path_of_folder)
	#move files!
	shutil.move(os.path.join(path,file), os.path.join(path_of_folder,file))

#BONUS
#function to display files and folders on the Desktop!
def DisplayFOD(path):
	list_of_folders = os.listdir(path)
	list_of_folders[:] = [d for d in list_of_folders if not d[0] == '.']
	print "\nComment: Following are the folders on your Desktop!\n"
	for l in list_of_folders:
		print l

#BONUS
#function to sort folders according to the data they hold!
def sortATD(path):
	DATATYPE = ['IMAGES','VIDEOS','TEXT','SYS','SPREADSHEET','PROG','PRESENTATION','INTERNET','EXECUTABLES','COMPRESSED','DATA']
	IMAGES = ['ANI','BMP','CAL','FAX','GIF','IMG','JBG','JPE','JPEG','JPG','MAC','PBM','PCD','PCX','PCT','PGM','PNG','PPM','PSD','RAS','TGA'',TIFF','WMF']
	VIDEOS = ['3G2','3GP','AVI','FLV','H264','M4V','MKV','MOV','MP4','MPG','MPEG','RM','SWF','VOB','WMV' ]
	TEXT = ['DOC','DOCX','ODT','PDF','RTF','TEX','TXT','WKS','WPS','WPD']
	SYS = ['BAK','CAB','CFG','CPL','CUR','DLL','DMP','DRV','ICNS','ICO','INI','LNK','MSI','SYS','TMP']
	SPREADSHEET = ['ODS','XLR','XLS','XLSX']
	PROG = ['PY','C','CLASS','CPP','CS','H','PHP','JAVA','SH','SWIFT','VB']
	PRESENTATION = ['KEY','ODP','PPS','PPT','PPTX']
	INTERNET = ['ASP','ASPX','CER','CFM','CGI','PL','CSS','HTM','HTML','JS','JSP','PART','RSS','XHTML']
	EXECUTABLES = ['APK','BIN','CGI','PL','COM','EXE','GADGET','JAR','WSF' ]
	COMPRESSED = ['7Z','ARJ','DEB','PKG','RAR','RPM','TAR','GZ','Z','ZIP']
	DATA = ['CSV','DAT','DB','DBF','LOG','MDB','SAV','SQL','XML','JSON']
	list_of_folders = os.listdir(path)
	list_of_folders[:] = [d for d in list_of_folders if not d[0] == '.']
	#print list_of_folders
	for l in list_of_folders:
		for d in DATATYPE:
			for ext in eval(d):
				if l == ext:
					if not os.path.exists(path+d):
						os.makedirs(path+d)
					shutil.move(os.path.join(path,l), os.path.join(path+d,l))
	print "Comment: Files sorted according to their data!"

#function to print top n files on your PC!
def printTNF():
	while(1):
		print "SCANNING MODE!"
		n = input('Enter how many top files of your system you want to view: ')
		if n==0:
			return
		print "\nComment: The top "+`n`+" files on your PC are:"
		#dictionary where key is path of the file and value is size in bytes!
		top_n_files = {}
		for i in range(1,n+1):
			top_n_files['a'+`i`] = 0
		
		#recursively search for folders and check their files sizes!
		for path, subdirs, files in os.walk(path_to_scan):
			#for excluding hidden files and folders!
			files = [f for f in files if not f[0] == '.']
			subdirs[:] = [d for d in subdirs if not d[0] == '.']
			#iterate over list of files in a particular folder!
			for file in files:
				try:
					fsize = os.path.getsize(path+delimiter+file)
					key_min = min(top_n_files.keys(), key=(lambda k: top_n_files[k]))
					if fsize > top_n_files[key_min]:
						del top_n_files[key_min]
						top_n_files[path+delimiter+file] = fsize
				except OSError:
					pass

		#list of tuples of top n file paths and sizes! 
		top_n_files = sorted(top_n_files.items(), key=lambda x:x[1] , reverse = True)

		print "Size\t\tFile Name:\n"
		#print top 10 files!
		for x in top_n_files:
			var = x[1]/1048576
			print "%.2f" %var,
			print "MB\t"+ x[0]

		#list containing top n files
		top_n_file_names = []
		for x in top_n_files:
			top_n_file_names.append(x[0])
		
		#BONUS
		#Avail extra usability
		while(1):
			try:
				x = input("\nDo you want to: \n1) Sort these files in the order of least to most recently used(modified)\n2) Go back to main menu\n")
				#x = x[0].lower()
				if x == 1:
					sortedFilesLeastToMost = sorted(top_n_file_names, key=os.path.getctime)
					print "\nComment: Following is the list of top n files in the order of least to most recently used!\n"
					i = 1
					for file in sortedFilesLeastToMost:
						print i,
						print " "+file
						i = i+1
					break
				elif x == 2:
					return
				else:
					print "Comment: Invalid Operation!"
			except:
				print "Comment: Invalid Operation!"
		try:
			u = raw_input("Type 'Y' to stay in this SCANNING MODE or 'N' to move back to MAIN MENU?(Y/N): ")
			u = u[0].lower()
			if u =='y':
				pass
			elif u == 'n':
				return
			else:
				print "Comment: Invalid Operation!"
		except:
			print "Comment: Invalid Operation!"

#function to sort files on Desktop according to their extensions!
def moveFAE():
	#list of all the valid extensions!
	VALID_EXTENSIONS = ['ANI','BMP','CAL','FAX','GIF','IMG','JBG','JPE','JPEG','JPG','MAC','PBM','PCD','PCX','PCT','PGM','PNG',
	'PPM','PSD','RAS','TGA'',TIFF','WMF','3G2','3GP','AVI','FLV','H264','M4V','MKV','MOV','MP4','MPG','MPEG','RM','SWF','VOB',
	'WMV','DOC','DOCX','ODT','PDF','RTF','TEX','TXT','WKS','WPS','WPD','BAK','CAB','CFG','CPL','CUR','DLL','DMP','DRV','ICNS',
	'ICO','INI','LNK','MSI','SYS','TMP','ODS','XLR','XLS','XLSX','PY','C','CLASS','CPP','CS','H','PHP','JAVA','SH','SWIFT','VB',
	'KEY','ODP','PPS','PPT','PPTX','ASP','ASPX','CER','CFM','CGI','PL','CSS','HTM','HTML','JS','JSP','PART','RSS','XHTML',
	'APK','BIN','CGI','PL','COM','EXE','GADGET','JAR','WSF','7Z','ARJ','DEB','PKG','RAR','RPM','TAR','GZ','Z','ZIP'
	,'CSV','DAT','DB','DBF','LOG','MDB','SAV','SQL','XML','JSON']
	home_name = os.path.expanduser('~')
	path = home_name + '/Desktop/'
	#list of all files and directories on Desktop
	list_of_files_dir = os.listdir(path)
	#list of files excluding shortcuts on Desktop
	files = [ f for f in list_of_files_dir if os.path.isfile(os.path.join(path,f)) and not os.path.islink(path+f)]
	
	while(1):
		print "SORTING MODE: "
		print "\nEnter the which kind of sorting you want or just want to print the Files/Folders on your Desktop!"
		try:
			type_of_sort = raw_input("a) Sort only according to the valid extensions?\nb) Sort according to any kinds of extensions?\nc) List files and folders on your Desktop?\nd) Sort these folders according to the type of data they hold like images etc.\ne)Exit SORTING MODE!\n")
			type_of_sort = type_of_sort[0]
			
			if type_of_sort == 'a' or type_of_sort == 'b':
				for file in files:
					#extract the extensions!
					ext = os.path.splitext(file)[1]
					if ext == '':
						#since no extensions files are considered as txt by default
						ext = '.txt'
					if type_of_sort == 'a':
						if ext.upper()[1:] in VALID_EXTENSIONS:
							moveFAEhelper(path,file,ext)
					else:
						moveFAEhelper(path,file,ext)
				print "Comment: Files on your Desktop sorted!"
			elif type_of_sort == 'c':
				DisplayFOD(path)
			elif type_of_sort == 'd':
				sortATD(path)
			elif type_of_sort == 'e':
				break
			else:
				print "Comment: Invalid Operation!"
		except:
			print "Comment: Invalid Operation!"

def main():
	print "Welcome to Infrastructure Management for Your PC!"
	while(1):
		try:
			inp = input('\nMAIN MENU: \nEnter the type of action you want to take!\n1) Get Top \'n\' files of your system according to their sizes!(Will take you to SCANNING MODE)\n2) Sort the files on Desktop according to the extensions!(Will take you to SORTING MODE)\n3) List duplicate files on your system\n4) Allow remote user to download files on this PC!\n5) Exit!\n')
			if inp == 1:
				#function to print the top n files!
				printTNF()
			elif inp == 2:
				#function to sort the Files on Desktop According to their Extensions!
				moveFAE()
			elif inp == 3:
				#function to print the duplicate files on your PC!
				print_duplicates()
			elif inp == 4:
				print "Type the following request on any browser on any remote machine connected to internet!\n"
				IP = get_ip()
				print "Server started!\n"
				print IP+":8000"
				on_server()
				
			elif inp == 5:
				break
			else:
				print "Comment: Invalid Operation!"
		except:
			print "Comment: Invalid Operation!"

if __name__ == "__main__":
    main()
