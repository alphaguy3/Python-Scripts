#Script Name:	openwebsite.py
#Author:	URJIT PATEL
#version:	1.2

import sys,webbrowser

if len(sys.argv) > 1:
	i = 1;
	while i < len(sys.argv):
		url = "https://" + sys.argv[i] + ".com"
		webbrowser.open_new_tab(url)
		i = i + 1

else:
	print 'Please Enter the website name'