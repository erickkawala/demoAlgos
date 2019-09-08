#!/usr/bin/python
# since package is nested under python version
# this can be useful
# esp with anaconda(conda) or venv

import sys

if (len(sys.argv) != 2):
    print("usage: python py_which.py <python_package>")
else:
    cmd1 = "import %s" % (sys.argv[1])
    exec(cmd1)
    cmd2 = "print(%s.__file__)" % (sys.argv[1])
    exec(cmd2)

sys.exit(2)
