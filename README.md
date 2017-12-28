# Overview
This script checks your Google Music library for missing songs. At least for me, every few months I find songs missing from my library. It turns out that Google is constantly updating its catalog, and, in the process, removes older versions of songs from your library. However, it doesn't automatically add newer versions back to your library. This script creates a list of songs in your library on first run, and compares the original list and new list on subsequent runs to let you know which songs are missing.

# Requirements

You must have Python installed on your system. You must also have pickle and gmusicapi modules installed

# Usage

To use, open up the py file with a text editor and add your Google username/password. On first run, create your database list when prompted. The database is a text file in the same directory. On subsequent run, skip the database list creation, or you'll overwrite the original database. The script will then find missing songs and added songs. Lastly, you can update the library at the end to include new songs added.
