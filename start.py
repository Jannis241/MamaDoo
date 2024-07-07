import os

print()
try:
    import flask

    print("Flask is already installed")
except:
    print("Import Module 'Flask' is missing..")
    print("Installing Flask now..")
    try:
        os.system(r"pip install -r requirements.txt")
        print("Installed requirements: successfully")
    except:
        raise Exception("Failed to install requirements")

from webseite import webseiteManager

webseiteManager.start()