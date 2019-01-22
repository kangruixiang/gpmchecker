#!/usr/bin/env python3

import os
import argparse
import json
from gmusicapi import Mobileclient
import codecs
import random

G = Mobileclient()
playlist = "51d6ea84-a1db-4202-aa5b-afb0fcb7b94d"

def login():
    """logs in to gmusic"""
    mc = Mobileclient()
    #mc.perform_oauth()
    G.oauth_login(Mobileclient.FROM_MAC_ADDRESS)

def getlibrary():
    """get all library from library"""
    library = G.get_all_songs()
    return library


def generaterandom(mylibrary):
    """generates 150 random songs"""
    randomsongs = random.sample(mylibrary, 200)
    return randomsongs

def removesongs():
    """removes old music"""
    playlists = G.get_all_user_playlist_contents()
    for randomplaylist in playlists:
        if playlist in randomplaylist.values():
            for song in randomplaylist["tracks"]:
                G.remove_entries_from_playlist(song["id"])
        else:
            print("Skipping playlist, {}".format(randomplaylist["name"]))

def addsongs(randomsong):
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
    print("Removing old songs")
    removesongs()
    randomsong = generaterandom(mylibrary)
    print("Adding new songs")
    addsongs(randomsong)

if __name__ == '__main__':
    main()
