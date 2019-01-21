#!/usr/bin/env python3

import os
import argparse
import json
from gmusicapi import Mobileclient
import codecs
import random

G = Mobileclient()
playlist = "51d6ea84-a1db-4202-aa5b-afb0fcb7b94d"
content = "playlist.json"

def login():
    """logs in to gmusic"""
    mc = Mobileclient()
    #mc.perform_oauth()
    G.oauth_login(Mobileclient.FROM_MAC_ADDRESS)

def getlibrary():
    """get all library from library"""
    library = G.get_all_songs()
    return library

def removesongs():
    """removes old music"""
    playlists = G.get_all_user_playlist_contents()
    return playlists

def savelibrary(playlists):
    """saves the library to a file"""
    if not os.path.exists(content):
        print(f'File \'{content}\' not found. Creating it.')
        with open(content, 'w', encoding='utf-8') as f:
            json.dump(playlists[0], f, sort_keys=True, indent=2)
    else:
        print("Library exists")

def main():
    login()
    mylibrary = getlibrary()
    playlists = removesongs()
    savelibrary(playlists)

if __name__ == '__main__':
    main()
