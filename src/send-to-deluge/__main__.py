import sys
import argparse
from .util.torrent_parser import TorrentParser
from .util.argparse_actions import CheckRemainingDiskSpaceAction

parser = argparse.ArgumentParser(description='Sends torrent files to deluge only if certain conditions are met.')
parser.add_argument('infile', type=str)
parser.add_argument('--check-disk-space', type=str, action=CheckRemainingDiskSpaceAction, dest='remaining_disk_space')
parser.add_argument('--deluge-host', type=str, dest='deluge_host', required=True)
parser.add_argument('--deluge-daemon-port', type=str, dest='deluge_daemon_port', required=True)
parser.add_argument('--deluge-username', type=str, dest='deluge_username', required=True)
parser.add_argument('--deluge-password', type=str, dest='deluge_password', required=True)

args = parser.parse_args()

torrent_parser = TorrentParser(args.infile)

torrent_size = torrent_parser.get_torrent_size()
torrent_name = torrent_parser.get_torrent_name()
remaining_disk_space = args.remaining_disk_space

print('Torrent size: %s %s' % (torrent_size / 1024 / 1024 / 1024, "GB"))
print('Remaining disk space: %s %s' % (remaining_disk_space / 1024 / 1024 / 1024, "GB"))

deluge_command = 'deluge-console "connect %s:%s %s %s ; add %s ; exit' \
                 % (args.deluge_host, args.deluge_daemon_port, args.deluge_username, args.deluge_password, args.infile)

if torrent_size > remaining_disk_space:
    print("Not enough remaining disk space. Ignoring torrent: %s" % torrent_name)
    sys.exit(1)
else:
    print("Sending to deluge: %s" % deluge_command)
    sys.exit(0)
