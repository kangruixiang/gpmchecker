# Overview

This script checks your Google Music playlists for missing songs. At least for me, every few months I find songs missing from my playlists. It turns out that Google is constantly updating its catalog, and, in the process, removes older versions of songs from your playlists. However, it doesn't automatically add newer versions back to your playlists. This script creates a list of songs in your playlists on first run, and compares the original list and new list on subsequent runs to let you know which songs are missing.

# Installation

## Python modules

The following modules are required:

- gmusicapi

To install:

```
  pip3 install gmusicapi
```

Alternatively, you can navigate to the current folder in command line and use 

```
pip3 install -r requirements.txt
```

# Usage

Double click on musicchecker.py and it will prompt you to login in web browser. On first run, a library.json will be saved with all of your songs. On subsequent runs, your current library will be compared to the library in library.json, and missing songs will be listed. You will be also prompted to update library.json at the end so it stays up to date.

