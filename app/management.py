""" This will have creation and checking access to the database """

import sqlite3

DB_FILE = "zetten.db"



def create_user(username, password):

    # NOTE TO FUTURE SELF PLANS:
    # PUT IN SOME TYPE OF HASHCODE
    # ADD IN PARAMETERS FOR PASS AND USERNAME SIZE
    # MAYBE ID FOR STORIES?

    with sqlite3.connect(DB_FILE) as db:

        c = db.cursor()

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username     TEXT,
                password     TEXT
            )
            """
        )

        c.execute(
            'INSERT INTO users(username, password) VALUES (\"%s\", \"%s\")' % (username, password)
        )
    
    return True

def authenticate_user(username, password):

    with sqlite3.connect(DB_FILE) as db:

        c = db.cursor()

        user_pw = c.execute(
            'SELECT password FROM `users` WHERE `users`.username = \"%s\"' % username
        ).fetchone()
        if user_pw is not None:
            print(user_pw[0])
            return user_pw[0] == password

    return False

def create