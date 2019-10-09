import os
libs = {'numpy','matplotlib','sklearn','requests',\
'jieba','beautifulsoup4','wheel','networkx','#spmpy',\
'django','flask','werobot','pyqt5',\
'pandas','pyopengl','pypdf2','docopt','pygame'}
for lib in libs:
    try:
        os.sysytem("pip install --user "+lib)
        print("Successfully")
    except:
        print("Failed")