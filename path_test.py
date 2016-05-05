import os

print ("abspath: " + os.path.abspath(__file__))

PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

print ("PROJECT_APP_PATH:" + PROJECT_APP_PATH)
print ("PROJECT_APP: " + PROJECT_APP)
print ("PROJECT_ROOT & BASE_DIR: " + PROJECT_ROOT)