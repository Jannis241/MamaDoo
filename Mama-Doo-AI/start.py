import sys
import os


sys.path.append('./webseite')
try:
    import flask
    print()
    print("Flask already installed: True")
except:
    print("Import Module 'Flask' is missing..")
    print()
    print()
    print("Installing Flask now..")
    print()
    try:
        os.system("pip install -r requirements.txt")
        print("Installed requirements: successfully")
    except:
        raise("Failed to install requirements")
import webseiteManager
webseiteManager.start()



