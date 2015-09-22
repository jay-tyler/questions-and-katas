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
    pass

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


class Bin(object):
    def __init__(index, lower_limit, bin_size):
        self.index       = index
        self.lower_limit = lower_limit
        self.upper_limit = lower_limit + bin_size

    def __contains__(self, val):
        return self.lower_limit <= val < self.upper_limit


class BinSet(object):
    def __init__(n_bins=1000, bins_dir='bins', lower_limit=-sys.maxsize, upper_limit=sys.maxsize):
        self.n_bins   = n_bins
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.bin_size = (2 * sys.maxsize) / N_HASH_BINS
        self.bins_dir = bins_dir
        self.files    = self.create_bins()

    def create_bins(self):
        file_cache = []
        for i in range(self.n_bins):
            lower_bin_limit = -sys.maxsize + i * self.bin_size
            filename = "{dir}/{bin}.txt".format(dir=self.bins_dir, bin=lower_bin_limit)
            with open(filename, 'w+') as file:
                file_cache.append(filename)
        return tuple(file_cache)

    def bin_index_for(val):
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
    pass