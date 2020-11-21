# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import OrderedDict

import bencodepy
import argparse
from functools import reduce

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('infile', type=argparse.FileType('rb'))

args = parser.parse_args()

torrent_info = dict(bencodepy.decode(args.infile.read()))

torrent_size = reduce(lambda length1, length2: length1+length2,
                      map(lambda file: file[b'length'], torrent_info[b'info'][b'files']))

print(torrent_size / 1024 / 1024 / 1024)
