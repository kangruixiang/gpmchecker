# Google Play Music to Spotify

This script generates a list of songs from your Google Play Music library so that you can export your library to spotify. The transfer process involves 2 steps:

1. Generate a list of songs in your library via this script
2. Import list into spotify using [PlaylistConverter](http://www.playlist-converter.net/#/).

This script has been forked from [cjbassi](https://github.com/cjbassi/gpm-library-checker)'s gpm library checker.

# Generate list of songs

## Installation

Make sure you have [python installed](https://realpython.com/installing-python/).

Requires [gmusicapi](https://github.com/simon-weber/gmusicapi) which you can install using either virtualenv or with:

```sh
pip3 install --user gmusicapi
```

Or on some systems you can use:
```sh
pip install --user gmusicapi
```

If you're getting an error about gmusicapi not being found after running the above command, then you need to configure your $PATH to support user installs. If you're on Linux (and possible OSX), you need to add:

```sh
export PATH=$PATH:~/.local/bin
```

to your shell config and reload your shell.


## Usage

First, `git clone` this repo:

```sh
git clone https://github.com/thisispiggy/gpmtospotify
```

Run the script with your Google email and password as command line arguments.

```sh
./path/to/script/gpmtospotify.py email password
```

The script will create a `gpm_library.json` file on first run. Open the library with a text editor other than notepad such as wordpad or Visual Studio Code. You should see a list of songs and artists.

# Import to Spotify

Head over to [PlaylistConverter](http://www.playlist-converter.net/#/) and paste your list of songs into the textbox. Click Convert and click on the Spotify option. The converter will connect to your spotify account and begin the importing process.