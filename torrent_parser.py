from functools import reduce

import bencodepy


class TorrentParser:
    def __init__(self, torrent_file):
        with open(torrent_file, "rb") as f:
            self.torrent_info = dict(bencodepy.decode(f.read()))

    def get_torrent_size(self):
        return reduce(lambda length1, length2: length1 + length2,
                      map(lambda file: file[b'length'], self.torrent_info[b'info'][b'files']))

    def get_torrent_name(self):
        return self.torrent_info[b'info'][b'name'].decode()
