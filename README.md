# Overview
This script checks your Google Music library for missing songs. At least for me, every few months I find songs missing from my library. It turns out that Google is constantly updating its catalog, and, in the process, removes older versions of songs from your library. However, it doesn't automatically add newer versions back to your library. This script creates a list of songs in your library on first run, and compares the original list and new list on subsequent runs to let you know which songs are missing.

This script has been tested on Mac OS Sierra.

# Installation

## Python

Python 2 comes installed by default on Mac and needs to be updated to 3. To do so, headover to https://www.python.org/downloads/ and download the latest version. After you follow the instructions and install python, open up the Terminal and type "python3." You should see something similar to this:

```
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```



## Python modules

The following modules are required:

- pickle
- gmusicapi

To install both, open up terminal/cmd and type:

```
  pip3 install pickle gmusicapi
```

# Usage

To use, open up Terminal. Type "python3" and drag the script file into the terminal, follow that with your username and password. For example, say the script is in your Downloads folder, and your username is Bob and password hunter2, your terminal should look like this:

```
  python3 /Users/Bob/Downloads/gmusicchecker.py Bob hunter2
```

Press enter. The script will create a library.txt file on first run with a list of song names, albums, artist, and unique ID. On subsequent runs, the script will compare your current library to existing one in library.txt and list the missing songs as well as new songs added. This gives you a chance to re-add the missing songs manually in Google Music. Lastly, the script will ask if you want to update the library. This overwrites the original library.txt with the current one.
