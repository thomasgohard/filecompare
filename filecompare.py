# coding: utf-8

"""
filecompare
~~~~~~~~~~~

Compares files; tells you whether they're the same or different.

Copyright: © 2015 Thomas Gohard
Licence: MIT, see LICENSE for details

"""

__title__ = 'filecompare'
__version__ = '0.1-dev'
__author__ = 'Thomas Gohard'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Thomas Gohard'



import argparse
from os.path import isfile
from os.path import getsize



"""
global variables
----------------
path1: The path of the first file.
path2: The path of the second file.
show_same: Output result of comparison if files are the same (default: True).
show_different: Output result of comparison if files are different (default: True).
"""

path1 = ""
path2 = ""
show_same = True
show_different = True



"""
helper functions
----------------
"""

def err_FNF(path):
    """Displays an error and exits when a file is not found.

    Parameters:
        path: A string containing the path to the file.

    Returns:
        -1 to indicate an error occurred.
    """
    print "Error: " + path + " does not exist."
    exit(-1)



"""
main code
---------
"""

argparser = argparse.ArgumentParser(description="Compare files; tell whether they're the same or different.")
output_opts = argparser.add_mutually_exclusive_group()
output_opts.add_argument("--show-same-only", action="store_true")
output_opts.add_argument("--show-different-only", action="store_true")
argparser.add_argument("path1", type=str)
argparser.add_argument("path2", type=str)
args = argparser.parse_args()

path1 = args.path1
path2 = args.path2
if args.show_same_only:
    show_different = False
if args.show_different_only:
    show_same = False

if not isfile(path1):
    err_FNF(path1)

if not isfile(path2):
    err_FNF(path2)

if getsize(path1) != getsize(path2):
    if show_different:
        print path1 + "\t!\t" + path2
    exit(0)

f1 = open(path1, "rb")
f2 = open(path2, "rb")

for b1 in iter(f1.read(1)):
    b2 = f2.read(1)

    if b2 != b1:
        if show_different:
            print path1 + "\t!\t" + path2
        exit(0)

if show_same:
    print path1 + "\t=\t" + path2
exit(1)
