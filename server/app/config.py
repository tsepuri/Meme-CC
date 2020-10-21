import sys
from .db import seed
def dbseed():
    inputs = int(input("Number of images to seed?\n"))
    
    if inputs > 1000:
        inputs = 1000
    #seed.load_init(limit=3*(inputs/6), time_filter='day', media=['reddit'])
    #seed.load_init(limit=inputs/6, time_filter='week', media=['reddit'])
    # Currently does not return exact number of requested images since Twitter API doesn't allow enough access
    seed.load_init(limit=inputs/2, media=['twitter'])
if __name__ == '__main__':
    sys.exit(dbseed())