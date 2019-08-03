#!/usr/bin/python

import sys


if (len(sys.argv) != 2):
    print("usage:  sizeOf <object> ")
else:
    obj = sys.argv[1]
    size = sys.getsizeof(obj)
    print(size)

sys.exit(2)
