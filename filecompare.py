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



"""
global variables
----------------
path1: The path of the first file.
path2: The path of the second file.
"""

path1 = ""
path2 = ""



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

if getFileSize(path1) != getFileSize(path2):
    print "The files are different: File size is different."
    exit(0)

f1 = open(path1, "rb")
f2 = open(path2, "rb")

for b1 in iter(f1.read(1)):
    b2 = f2.read(1)

    if b2 != b1:
        print "The files are different: File contents are different."
        exit(0)

print "The files are the same."
exit(1)
