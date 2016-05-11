import os

print ("abspath: " + os.path.abspath(__file__))

PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
# MEDIA_URL = STATIC_URL + "media/"
AWS_STORAGE_BUCKET_NAME = 'ssmm-static'
MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))



print ("PROJECT_APP_PATH:" + PROJECT_APP_PATH)
print ("PROJECT_APP: " + PROJECT_APP)
print ("PROJECT_ROOT & BASE_DIR: " + PROJECT_ROOT)
print ("MEDIA_URL: " + MEDIA_URL)
print ("MEDIA_ROOT: " + MEDIA_ROOT)
