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

def getFileSize(path):
    """Get the size of a file.

    Parameters:
        path: A string containing the path to the file.

    Returns:
        The size of the file in bytes.
    """
    f = open(path, "rb")
    f.seek(0, 2)
    size = f.tell()
    f.close()

    return size



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

if getFileSize(path1) != getFileSize(path2):
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
