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
    
    return True

def authenticate_user(username, password):

    with sqlite3.connect(DB_FILE) as db:

        c = db.cursor()

        user_pw = c.execute(
            "SELECT password FROM users WHERE username=:username",
            {"username": username},
        ).fetchone()
        
        if user_pw is not None:
            return user_pw[0] == password

    return True