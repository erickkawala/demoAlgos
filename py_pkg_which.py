#!/usr/bin/python
# since package is nested under python version
# this can be useful
# esp with anaconda(conda) or venv

import sys

a = sys.argv

# no argv yet? for multiple args

def func(arg):
    if (len(sys.argv) != 2):
        print("usage: python py_which.py <python_module>")
        return
    else:
        cmd1 = "import %s" % (sys.argv[1])
        exec(cmd1)
        cmd2 = "print(%s.__file__)" % (sys.argv[1])
        exec(cmd2)

func(sys.argv[1])
# can't try catch an import =( so no
# except SyntaxError: "usage:"
# when arg is not a python module

sys.exit(2)
