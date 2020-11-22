import argparse
import shutil


class CheckRemainingDiskSpaceAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(CheckRemainingDiskSpaceAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        total, used, free = shutil.disk_usage(values)
        setattr(namespace, self.dest, free)