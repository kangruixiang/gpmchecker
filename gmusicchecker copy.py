from gmusicapi import Mobileclient
import pickle
import argparse
import os


"""Adds arguments"""

# Adds arguments to command line

parser = argparse.ArgumentParser()

parser.add_argument('username', action='store',
                    help='Stores username')
parser.add_argument('password', action='store',
                    help='Stores password')

authentication = parser.parse_args()


"""Logs in and retrieves library"""

api = Mobileclient()
logged_in = api.login(authentication.username, authentication.password, Mobileclient.FROM_MAC_ADDRESS)

library = api.get_all_songs()



"""Creates the library.txt if not exist"""

if not os.path.exists('library.txt'):
    f = open('library.txt', 'w')
    f.close()
    print('No library.txt found. Creating a new one.')

def comp(old, new):

    # Compares old library with new library

    print('Checking songs missing:')
    for val in old:
        if val not in new:
            print('missing song: ' + val)
    print('-' * 10 + '\nChecking new songs added:')
    for val in new:
        if val not in old:
            print('new song added: ' + val)

def update():

    # Overwrites existing library with new library

    f = open('library.txt', 'w', encoding='utf-8')

    for i in library:
        f.write("{} artist: {} album: {} id: {}\n".format(str(i['title']), str(i['artist']), str(i['album']), str(i['id'])))

    f.close()

def main():

    arguments()
    client()
    library()
    # Old library

    oldsongs = []
    with open("library.txt", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            oldsongs.append(line)

    # New library

    newsongs = []
    for i in library:
        newsongs.append("{} artist: {} album: {} id: {}".format(str(i['title']), str(i['artist']), str(i['album']), str(i['id'])))

    comp(oldsongs, newsongs)
    print('-' * 10 + '\nPress 1 for updating library. Otherwise close the window to exit')
    updatelibrary = input()
    if updatelibrary == '1':
        update()
        print('Finished updating library!')
    else:
        print('Done!')

if __name__ == '__main__':
    main()
