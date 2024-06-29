import sys
import os


sys.path.append('./webseite')
os.system("pip install -r requirements.txt")
os.remove("requirements.txt")
import webseiteManager
webseiteManager.start()



