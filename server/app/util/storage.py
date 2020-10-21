from dotenv import  load_dotenv
import os
from . import reddit, settings
import urllib.request
from flask import redirect, send_file
import shutil
load_dotenv()
def storeImage(url, file_name, restart=False):
    if os.getenv('LOCAL') == "true":
        PATH = os.path.join(os.getenv('LOCAL_PATH'),"images")
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        if restart:
            if len(PATH) > 0:
                if input("The images folder will be cleared irreversibly. Proceed? Y/n").lower() != 'y':
                    return
        PATH = os.path.join(PATH, file_name)
        urllib.request.urlretrieve(url, PATH)
    elif os.getenv('S3') == "true":
        '''
        under construction
        '''
def getImage(post_information):
    if os.getenv('LOCAL') == "true":
        PATH = os.path.join(os.getenv('LOCAL_PATH'),"images")
        if not os.path.exists(PATH):
            return FileNotFoundError
        PATH = os.path.join(PATH, post_information.file_name)
        if not os.path.exists(PATH):
            return FileNotFoundError
        return send_file(PATH)
    elif os.getenv('ONLINE') == "true":
        if not post_information.url:
            return FileNotFoundError
        return redirect(post_information.url)
def clean():
    if os.getenv('LOCAL') == "true":
        PATH = os.path.join(os.getenv('LOCAL_PATH'),"images")
        shutil.rmtree(PATH) 
        os.mkdir(PATH)