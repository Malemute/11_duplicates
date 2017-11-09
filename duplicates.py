import sys
import os
from collections import Counter


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('{} <filename>'.format(sys.argv[0]))

    dirpath = sys.argv[1]
    for top, dirs, files in os.walk(dirpath):
        for nm in files:
            print(os.path.join(top, nm))
