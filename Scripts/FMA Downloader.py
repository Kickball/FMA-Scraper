import os, sys

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

URLs = []
files = os.listdir(getScriptPath())

for file in files:
	if os.path.splitext(file)[1] == '.fma':
		directory = os.path.splitext(file)[0]
		if not os.path.exists(getScriptPath() + '\\' + directory):
			os.makedirs(directory)
		with open(file) as f:
			URLs = f.readlines()
        for URL in URLs:
            os.system('python -m wget -o %s %s' %(directory, URL))
