from gmusicapi import Mobileclient
import pickle

api = Mobileclient()
logged_in = api.login('google username', 'google password', Mobileclient.FROM_MAC_ADDRESS)
library = api.get_all_songs()

def update():
    f = open('library.txt', 'w', encoding='utf-8')
    for i in library:
        f.write(str(i['title']) + ', ' + str(i['id']) + '\n')
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

def main():

    print('Press 1 to make new database. Press any other key to skip this step')
    if input() == '1':
        update()

    oldsongs = []
    with open("library.txt", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            oldsongs.append(line)

    newsongs = []
    for i in library:
        newsongs.append(str(i['title']) + ', ' + str(i['id']))

    comp(oldsongs, newsongs)
    print('-' * 10 + '\nPress 1 to updating library')
    updatelibrary = input()
    if updatelibrary == '1':
        update()
        print('Finished updating library!')
    else:
        print('Done!')

main()
