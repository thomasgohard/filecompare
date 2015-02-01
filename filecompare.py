# coding: utf-8

"""
filecompare
~~~~~~~~~~~

Compares files; tells you whether they're the same or different.

Copyright: © 2015 Thomas Gohard
Licence: MIT, see LICENSE for details

"""

__title__ = 'filecompare'
__version__ = '0.2-dev'
__author__ = 'Thomas Gohard'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Thomas Gohard'



import argparse
from os.path import exists
from os.path import isdir
from os.path import isfile
from os.path import getsize



"""
global variables
----------------
path1: The path of the first file or directory.
path2: The path of the second file or directory.
recursive: Recursively compare directories (default: False).
show_same: Output result of comparison if files are the same (default: True).
show_different: Output result of comparison if files are different (default: True).
"""

path1 = ""
path2 = ""
recursive = False
show_same = True
show_different = True



"""
helper functions
----------------
"""

def err_PNF(path):
    """Displays an error and exits when a path is not found.

    Parameters:
        path: A string containing the path.

    Returns:
        -1 to indicate an error occurred.
    """
    print "Error: " + path + " does not exist."
    exit(-1)

def err_PTNM():
    """Displays an error and exists when the types of paths do not match.

    Parameters: None.

    Returns:
        -1 to indicate an error occurred.
    """
    print "Error: Cannot compare a file to a directory."
    exit(-1)

def warn_NAF(option):
    """Displays a warning when an option is not applicable when comparing files.

    Parameters:
        option: The option that is not applicable.

    Returns:
        Nothing
    """
    print "Warning: Option " + option + " is not applicable when comparing files."

def cmp_files(path1, path2):
    """Compares two files.

    Parameters:
        path1: The path to the first file to compare.
        path2: The path to the second file to compare.

    Returns:
        True if the files are the same, false otherwise.
    """
    if getsize(path1) != getsize(path2):
        if show_different:
            print path1 + "\t!\t" + path2
        return False

    f1 = open(path1, "rb")
    f2 = open(path2, "rb")

    for b1 in iter(f1.read(1)):
        b2 = f2.read(1)

        if b2 != b1:
            if show_different:
                print path1 + "\t!\t" + path2
            return False

    if show_same:
        print path1 + "\t=\t" + path2
    return True

def cmp_dirs(path1, path2):
    """Compares two directories.

    Parameters:
        path1: The path to the first directory to compare.
        path2: The path to the second directory to compare.

    Returns: Nothing
    """



"""
main code
---------
"""

argparser = argparse.ArgumentParser(description="Compare files; tell whether they're the same or different.")
output_opts = argparser.add_mutually_exclusive_group()
output_opts.add_argument("--show-same-only", action="store_true")
output_opts.add_argument("--show-different-only", action="store_true")
argparser.add_argument("-r", action="store_true")
argparser.add_argument("path1", type=str)
argparser.add_argument("path2", type=str)
args = argparser.parse_args()

path1 = args.path1
path2 = args.path2
if args.r:
    recursive = True
if args.show_same_only:
    show_different = False
if args.show_different_only:
    show_same = False

if not exists(path1):
    err_PNF(path1)

if not exists(path2):
    err_PNF(path2)

if (isdir(path1) and isfile(path2)) or (isfile(path1) and isdir(path2))
    err_PTNM()

if isfile(path1) and isfile(path2):
    if recursive:
        warn_NAF("-r")
    result = cmp_files(path1, path2)
