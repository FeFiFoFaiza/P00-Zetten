""" DOES ALL THE SQL STUFF SO I DONT HAVE TO KEEP ON WRITING THE SAME THING OVER AGAIN"""

import sqlite3

DB_FILE = "zetten.db"

def execute(command):

    with sqlite3.connect(DB_FILE) as db:

            c = db.cursor()
            result = c.execute(command)
            db.commit()
    
    return result

def setup():

    execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id           INTEGER PRIMARY KEY,
                    username     TEXT,
                    password     TEXT
                )
                """
            )

    execute(
                """
                CREATE TABLE IF NOT EXISTS story_db (
                    id          INTEGER PRIMARY KEY,
                    storyID     INTEGER,
                    content     TEXT,
                    usrID       INTEGER
                )
                """
            )

    execute(
                """
                CREATE TABLE IF NOT EXISTS stories (
                    storyID     INTEGER PRIMARY KEY,
                    title       TEXT,
                    summary     TEXT,
                    usrID       INTEGER
                )
                """
            )

    
        