#!/usr/bin/env python3

import os
import argparse
import json
from gmusicapi import Mobileclient
import codecs

library = 'library.json'
missingsongs = 'missingsongs.json'
songs = 'gpm_library.json'
G = Mobileclient()

def login():
    """logs in to gmusic"""
    G.perform_oauth(open_browser=True)
    G.oauth_login(Mobileclient.FROM_MAC_ADDRESS)

def getlibrary():
    """get all songs from library"""
    
    library = G.get_all_songs()
    return library

def savelibrary(songs):
    """saves the library to a file"""
    if not os.path.exists(library):
        print(f'File \'{library}\' not found. Creating it.')
        with open(library, 'w', encoding='utf-8') as f:
            json.dump(songs, f, sort_keys=True, indent=2)
    else:
        print("Library exists")

def loadlibrary(filename):
    """loads library for checking"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)    

def getnewsongs():
    """gets new library"""
    newlibrary = G.get_all_songs()
    return newlibrary

def comparesongs(oldlibrary):
    oldsongs = []
    for song in oldlibrary:
        line = "{} - {}".format(song["title"], song["artist"])
        oldsongs.append(line)
    newlibrary = getnewsongs()
    newsongs = []
    for song in newlibrary:
        line = "{} - {}".format(song["title"], song["artist"])
        newsongs.append(line)
    removedsongs = [song for song in oldsongs if song not in newsongs]
    with open(missingsongs, 'w', encoding='utf-8') as f:
            json.dump(removedsongs, f, sort_keys=True, indent=2)
    return removedsongs

def addedsongs(oldlibrary):
    oldsongs = []
    for song in oldlibrary:
        line = "{} - {}".format(song["title"], song["artist"])
        oldsongs.append(line)
    newlibrary = getnewsongs()
    newsongs = []
    for song in newlibrary:
        line = "{} - {}".format(song["title"], song["artist"])
        newsongs.append(line)
    addedsongs = [song for song in newsongs if song not in oldsongs]
    return addedsongs
    
def updatelibrary(songs):
    with open(library, 'w', encoding='utf-8') as f:
            json.dump(songs, f, sort_keys=True, indent=2)

def main():
    login()
    mylibrary = getlibrary()
    savelibrary(mylibrary)
    oldlibrary = loadlibrary(library)
    print("--------------\nMissings songs:")
    print("\n".join(comparesongs(oldlibrary)))
    print("--------------\nAdded songs:")
    print("\n".join(addedsongs(oldlibrary)))
    mylibrary = getlibrary()
    update = input("--------------\nPress 1 to update library\nPress 2 to exit\n")
    if int(update) == 1:
        updatelibrary(mylibrary)
        print("--------------\nLibrary updated")
    else:
        pass
    

if __name__ == '__main__':
    main()
