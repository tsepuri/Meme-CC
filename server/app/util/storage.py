from dotenv import  load_dotenv
import os
import urllib.request
load_dotenv()
def storeImage(url, file_name, restart=False):
    if os.getenv('LOCAL'):
        PATH = os.path.join(os.getenv('LOCAL_PATH'),"images")
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        if restart:
            if len(PATH) > 0:
                if input("The images folder will be cleared irreversibly. Proceed? Y/n").lower() != 'y':
                    return
        PATH = os.path.join(PATH, file_name)
        urllib.request.urlretrieve(url, PATH)
    elif os.getenv('S3'):
        '''
        under construction
        '''
def getImage(file_name):
    if os.getenv('LOCAL'):
        PATH = os.path.join(os.getenv('LOCAL_PATH'),"images")
        if not os.path.exists(PATH):
            return FileNotFoundError
        PATH = os.path.join(PATH, file_name)
        if not os.path.exists(PATH):
            return FileNotFoundError
        return PATH