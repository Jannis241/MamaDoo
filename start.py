import os
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
        os.system(r"pip install -r requirements.txt")
        print("Installed requirements: successfully")
    except:
        raise Exception("Failed to install requirements")
try:
    from webseite import webseiteManager
    webseiteManager.start()

except:
    raise Exception("Failed to import webseiteManager")