import argparse
import shutil
from functools import reduce
import bencodepy


class CheckRemainingDiskSpaceAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(CheckRemainingDiskSpaceAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        total, used, free = shutil.disk_usage(values)
        setattr(namespace, self.dest, free)


class ExtractTorrentSizeAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        for key in kwargs:
            if key == 'type':
                if not isinstance(kwargs[key], argparse.FileType):
                    raise ValueError("Only arguments of type %s are allowed" % argparse.FileType)
        super(ExtractTorrentSizeAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        torrent_info = dict(bencodepy.decode(values.read()))
        torrent_size = reduce(lambda length1, length2: length1 + length2,
                              map(lambda file: file[b'length'], torrent_info[b'info'][b'files']))
        setattr(namespace, self.dest, torrent_size)
