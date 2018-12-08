#!/usr/bin/env python3

import os
import argparse
import json
from gmusicapi import Mobileclient
import codecs

LIBRARY = 'gpm_library.json'

def touch_file(name):
    """
    Creates a file if it doesn't exist and returns a bool telling if the file
    existed.
    """
    if not os.path.exists(name):
        print(f'File \'{name}\' not found. Creating it.')
        with open(name, 'w'):
            pass
        return False
    return True


def file_read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def file_write_json(filename, container):
    file = codecs.open(filename, 'w', 'utf-8')
    file.write(container)
    file.close()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', action='store',
                        help='Stores username')
    parser.add_argument('password', action='store',
                        help='Stores password')
    return parser.parse_args()


def authenticate(username, password):
    api = Mobileclient()
    api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
    return api


def get_songs(library):
    """Returns a new library of songs that only include artist, song, and album"""
    songs = []
    for song in library:
        title, artist = song['title'], song['artist']
        songs.append('{} - {}'.format(title, artist))
    songs2 = '\n'.join(songs)
    return songs2

def main():
    args = parse_args()
    username, password = args.username, args.password

    api = authenticate(username, password)
    library = api.get_all_songs()

    existed = touch_file(LIBRARY)

    new_songs = get_songs(library)
    if existed:
        old_songs = file_read_json(LIBRARY)
        removed_songs = [song for song in old_songs if song not in new_songs]

        print(str(len(removed_songs)) + ' ' + ('songs' if len(removed_songs) != 1 else 'song') + ' removed.')

        if len(removed_songs) > 0:
            touch_file(REMOVED)
            write_removed_songs(removed_songs)

    file_write_json(LIBRARY, new_songs)
    print('Updated library')


if __name__ == '__main__':
    main()
