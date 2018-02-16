# INFRASTRUCTURE ENGINEERING ASSIGNMENT

## BRIEF DESCRIPTION:
Program/Script in Python. The main focus kept in mind is to manage the PC's files.

## Main Functionalities:
Its a tool that scans your PC's files and folders and displays the top files according to their sizes. It also sorts the files on the Desktop according to their extensions and keep them in their extension named folder(option given to sort based only on the valid extensions or any extensions.) additionally it also moves them into folders named according to the kind of data they hold like images etc. It also allows remote users to download the files on this PC. It also lists the duplicate files on you system. It also sorts the files according to the least to most recently used files.

## Working Flow:
It basically has three modes:
1)MAIN MENU MODE:
	The tool starts in this mode. Here the following options are provided:
	1) Display top n files on the system(Enters into Scanning Mode).
	2) Sort files on Desktop according to extensions(Enters into Sorting Mode).
	3) List the duplicate files on your system.(ADDITIONAL)
	4) Allow remote user to download files on this PC.(ADDITIONAL)
	5) Exit.

2)SCANNING MODE:
	It displays the top n files on the system and provides additional functionalities like:
	1) Enter how many top files to be displayed according to their sizes. 
	2) Sort these top n files in the order of least to most recently used file.(ADDITIONAL)
	3) Exit SCANNING MODE.

3)SORTING MODE:
	It provides the kind of sorting among following the user want or just display the content of Desktop.
	1) Sort according to only valid extensions. (ADDITIONAL)
	2) Sort according to any kinds of extensions.
	3) List Files and Folders on Desktop. (ADDITIONAL)
	4) Sort according to the type of data they hold(Works after using either of the first two options) (ADDITIONAL)
	5) Exit SORTING MODE.

## ADDITIONAL FUNCTIONS:
1) get_ip():
	Returns the public IP of which the file is running.
2) on_server():
	Starts the HTTP Server to allow remote user to download files on this PC. 
3) read_chunks():
	Take the file descripter and returns it in chunks of size 1024.
4) print_duplicates():
	Prints the duplicate files. It uses hashlib module and sha1 algorithm and uses read_chunks() function.
5) moveFAEhelper():
	Helper function to which takes path, file name, and extension and moves the files according to their extensions.
6) DisplayFOD():
	Takes path and displays the files and folders on your system.
7) sortATD():
	Takes path and sorts the files on that part according to the data they hold like images etc.(Works after sorting them according to their extensions)
8) printTNF():
	Function to print top files of the system. Takes user to SCANNING MODE. It uses zip_file() function.
9) moveFAE():
	Function to sort the files on Desktop according to their extension, uses moveFAEhelper(), DisplayFOD(), sortATD() function.

## COMMAND TO RUN:
python Infra_manage.py

## LIBRARIES USED:
1) os
2) shutil
3) sys
4) platform
5) hashlib 
6) socket
7) call

## LANGUAGE USED:
Python 2.7.12

## PLATFORMS SUPPORTED:
1) Linux.
2) Windows.
