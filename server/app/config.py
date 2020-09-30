import sys
from .db import seed
def dbseed():
    inputs = int(input("Number of images to seed?\n"))
    if inputs > 1000:
        inputs = 1000
    seed.load_init(limit=inputs/2, time_filter='day')
    seed.load_init(limit=inputs/2, time_filter='week')
if __name__ == '__main__':
    sys.exit(dbseed())