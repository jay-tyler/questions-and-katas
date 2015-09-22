"""Helpful facts:
    builtin hash() yields an int object of 36 bytes
    100 character unicode string is an object of ~149 bytes
"""

strings = set()

#TODO: remove hard-coding to file link below.

# Option a. Smallbeans.
with open('corpus.txt') as file:
    for line in file:
        strings.add(line.rstrip('\n'))

def check_membership(string):
    return string in strings

# Option b. First part is to store the file as according to a hash-based algorithm
import sys

N_HASH_BINS = 1000  # Will result in ~3 strings per file for our 'corpus.txt'
BIN_SIZE = (2 * sys.maxsize) / N_HASH_BINS  # sys.maxsize signed; TODO: check implementation of sys.maxsize in Py2.x
BIN_DIR = 'bins'
FILES = []

def create_bins():
    for i in range(N_HASH_BINS):
        lower_bin_limit = -sys.maxsize + i * BIN_SIZE
        filename = "{dir}/{bin}.txt".format(dir=BIN_DIR, bin=lower_bin_limit)
        with open(filename, 'w+') as file:
            FILES.append(filename)

FILES = tuple(FILES)

def bin_for_index():

def get_bin_index(hashed):
    """Return int index associated with int hashed"""
    lower_limit = -sys.maxsize
    i = 0

    for i in range(N_HASH_BINS):
        if lower_limit <= hashed < (lower_limit + BIN_SIZE):
            break
        i += 1
        lower_limit = -sys.maxsize + i * BIN_SIZE  # TODO: Repeated expression; wrap into function

    return i

if __name__ == "__main__":
    create_bins()