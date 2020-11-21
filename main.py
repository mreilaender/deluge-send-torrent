import bencodepy
import argparse
from functools import reduce

parser = argparse.ArgumentParser(description='Sends torrent files to deluge only if certain conditions are met.')
parser.add_argument('infile', type=argparse.FileType('rb'))

args = parser.parse_args()

torrent_info = dict(bencodepy.decode(args.infile.read()))

torrent_size = reduce(lambda length1, length2: length1+length2,
                      map(lambda file: file[b'length'], torrent_info[b'info'][b'files']))



print(torrent_size / 1024 / 1024 / 1024)
