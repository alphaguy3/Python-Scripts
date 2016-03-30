#Script Name:	sysinfo.py
#Author:	URJIT PATEL
#version:	1.0


import platform

systeminfo = {
	'Architecture': platform.architecture(),
	'Machine': platform.machine(),
	'node':	platform.node(),
	'Processor': platform.processor(),
	'Current Python Version': platform.python_version(),
	'OS': 	platform.system()
}

for j in systeminfo:
	info = j + ' : ' + str(systeminfo[j])
	print info