import sys
from .db import seed
def dbseed():
    inputs = int(input("Number of images to seed?\n"))
    # still testing API limits
    if inputs > 1000:
        inputs = 1000
    seed.load_init(limit=3*(inputs/4), time_filter='week', media=['reddit'])
    seed.load_init(limit=inputs/4, time_filter='day', media=['reddit'])
    seed.load_init(limit=inputs/2, time_filter='week', media=['twitter'])
if __name__ == '__main__':
    sys.exit(dbseed())