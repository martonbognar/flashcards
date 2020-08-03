#!/usr/bin/env python3

import sqlite3
from random import randint

def get_input():
    return input('[a]dd a new word / [p]lay / [q]uit\n')

conn = sqlite3.connect('dutch.sqlite3')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT, word TEXT UNIQUE, meaning TEXT)''')
conn.commit()

action = get_input()

while action != "q":
    print('-------------------------')
    if action == "a":
        word = input('New word: ')
        meaning = input('Meaning: ')
        cur.execute('INSERT INTO words (word, meaning) VALUES (?, ?)', [word, meaning])
        conn.commit()
    elif action == "p":
        cur.execute('SELECT count(id) FROM words')
        (count,) = cur.fetchone()
        rnd = randint(1, count)
        cur.execute('SELECT word, meaning FROM words WHERE id = ?', (rnd,))
        (word, meaning) = cur.fetchone()
        guess = input('What does "{}" mean?\n'.format(word))
        if guess == meaning:
            print('Good guess!')
        else:
            print('Incorrect')
    else:
        print('Unknown action')
    print('-------------------------')
    action = get_input()


conn.close()
