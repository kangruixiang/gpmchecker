import os
import argparse
import json
from gmusicapi import Mobileclient
import codecs
from randomsongs import login, getlibrary, removesongs

G = Mobileclient()
playlist = "4e92ab67-d4a1-4ddb-a2ac-cf5f04845333"

def login():
    """logs in to gmusic"""
    mc = Mobileclient()
    #mc.perform_oauth()
    G.oauth_login(Mobileclient.FROM_MAC_ADDRESS)

def getlibrary():
    """get all library from library"""
    library = G.get_all_songs()
    return library

def getplaylists():

    p = G.get_all_playlists()
    return p


def addsongs(songs):
    """adding songs to playlist"""
    songstoadd = []
    for songs in randomsong:
        song = songs["id"]
        try:
            if not songs["rating"] == "1":
                G.add_songs_to_playlist(playlist, song)
        except KeyError:
            G.add_songs_to_playlist(playlist, song)
    return randomsong


def main():
    login()
    mylibrary = getlibrary()
    print(mylibrary[0])
    # removesongs()
    # addsongs(mylibrary)


if __name__ == '__main__':
    main()

