import sys

from argparse_actions import CheckRemainingDiskSpaceAction, ExtractTorrentSizeAction
import argparse

parser = argparse.ArgumentParser(description='Sends torrent files to deluge only if certain conditions are met.')
parser.add_argument('infile', type=argparse.FileType('rb'), action=ExtractTorrentSizeAction)
parser.add_argument('--check-disk-space', type=str, action=CheckRemainingDiskSpaceAction, dest='remaining_disk_space')

args = parser.parse_args()

torrent_size = args.infile
remaining_disk_space = args.remaining_disk_space

print('Torrent size: %s %s' % (torrent_size / 1024 / 1024 / 1024, "GB"))
print('Remaining disk space: %s %s' % (remaining_disk_space / 1024 / 1024 / 1024, "GB"))

if torrent_size > remaining_disk_space:
    sys.exit(-1)
else:
    sys.exit(0)
