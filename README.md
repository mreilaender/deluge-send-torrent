# send-torrent-to-deluge
This is a CLI tool to send torrent files to deluge only if certain criteria are met.

## Installation

```commandline
pip install .
```


## Usage

### Arguments
| Argument | Description | Example |
| -------------        | ---------------------------------------------------------------------------------------------- | ------------------------------ |
| infile               | Torrent file to send to deluge                                                                 | /tmp/some.torrent.file.torrent |
| --deluge-host        | Host name of the deluge server                                                                 | deluge                         |
| --deluge-daemon-port | Port of the deluge daemon                                                                      | 58846                          |
| --deluge-username    | Username to use when connecting to deluge                                                      | test                           |
| --deluge-password    | Password                                                                                       | test                           |
| --check-disk-space   | Checks if there is enough disk space available and only then sends the torrent file to deluge  | /home/user/downloads           |