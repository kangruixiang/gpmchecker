from gmusicapi import Mobileclient
import pickle
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('username', action='store',
                    help='Store a simple value')
parser.add_argument('password', action='store',
                    help='Store a simple value')

authentication = parser.parse_args()

api = Mobileclient()
logged_in = api.login(authentication.username, authentication.password, Mobileclient.FROM_MAC_ADDRESS)

library = api.get_all_songs()
if not os.path.exists('library.txt'):
    f = open('library.txt', 'w')
    f.close()
    print('No library.txt found. Creating a new one.')

def update():

    f = open('library.txt', 'w', encoding='utf-8')

    for i in library:
        f.write("{} artist: {} album: {} id: {}\n".format(str(i['title']), str(i['artist']), str(i['album']), str(i['id'])))

    f.close()

def comp(old, new):

    print('Checking songs missing:')
    for val in old:
        if val not in new:
            print('missing song: ' + val)
    print('-' * 10 + '\nChecking new songs added:')
    for val in new:
        if val not in old:
            print('new song added: ' + val)

oldsongs = []
with open("library.txt", encoding='utf-8') as file:
    for line in file:
        line = line.strip() #or someother preprocessing
        oldsongs.append(line)
        #print("old songs:", oldsongs[0:5])

newsongs = []
for i in library:
    newsongs.append("{} artist: {} album: {} id: {}".format(str(i['title']), str(i['artist']), str(i['album']), str(i['id'])))
    #print("new songs:", newsongs[0:5])

def main():

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
