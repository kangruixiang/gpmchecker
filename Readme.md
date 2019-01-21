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

# Usage

To use, open up terminal and type "python3" and drag the script file into the terminal, follow that with your username and password. For example, say the script is in your Downloads folder, and your username is Bob and password hunter2, your terminal should look like this:

```
  python3 gmusicchecker.py
```

Press enter. You will be prompted for your password. The script will create a library.txt file on first run with a list of song names, albums, artist, and unique ID. On subsequent runs, the script will compare your current library to existing one in library.txt and list the missing songs as well as new songs added. This gives you a chance to re-add the missing songs manually in Google Music. Lastly, the script will ask if you want to update the library. This overwrites the original library.txt with the current one.