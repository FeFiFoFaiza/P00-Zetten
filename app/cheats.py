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
                    content     VARCHAR,
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

    execute(
                """
                INSERT INTO users (username, password)
                SELECT 'JAWorley', 'password'
                WHERE NOT EXISTS
                    (SELECT username, password
                    FROM users
                    WHERE username = 'JAWorley' AND password = 'password')
                """
    )

    execute(
                """
                INSERT INTO users (username, password)
                SELECT 'wwww', 'www'
                WHERE NOT EXISTS
                    (SELECT username, password
                    FROM users
                    WHERE username = 'wwww' AND password = 'www')
                """
    )

    execute( 
                """
                INSERT INTO story_db (storyID, content, usrID)
                SELECT '1', 'Harry had a plan to pay for his school books and other supplies. When he had gone to Diagon Alley with Ron and his parents last summer before the start of his fourth year, he had been dismayed to find his vault practically empty. There had been enough gold to get new robes and his potions kit, but that was all, and he had spent the year borrowing books and school supplies from his friends. Now that the school year was over, he had three months to find a job and earn enough money to buy what he needed for his fifth year. He could not borrow things from Ron and Hermiones potions kits as that was not allowed and each kit had just enough to get a student through one year of Potions class. He needed two Galleons for that alone, which meant he needed to earn two hundred pounds. Robes would be another hundred and fifty pounds if he got used ones, and books would be about three hundred pounds if he bought them all used.', '1'
                WHERE NOT EXISTS
                    (SELECT storyID, content, usrID
                    FROM story_db
                    WHERE storyID = '1' AND content = 'Harry had a plan to pay for his school books and other supplies. When he had gone to Diagon Alley with Ron and his parents last summer before the start of his fourth year, he had been dismayed to find his vault practically empty. There had been enough gold to get new robes and his potions kit, but that was all, and he had spent the year borrowing books and school supplies from his friends. Now that the school year was over, he had three months to find a job and earn enough money to buy what he needed for his fifth year. He could not borrow things from Ron and Hermiones potions kits as that was not allowed and each kit had just enough to get a student through one year of Potions class. He needed two Galleons for that alone, which meant he needed to earn two hundred pounds. Robes would be another hundred and fifty pounds if he got used ones, and books would be about three hundred pounds if he bought them all used.' AND usrID = '1')
                """
    ) 

    execute( 
                """
                INSERT INTO stories (title, summary, usrID)
                SELECT 'An Unusual Start to The Summer', 'This is a filler which I have stolen from a good story', '1'
                WHERE NOT EXISTS
                    (SELECT title, summary, usrID
                    FROM stories
                    WHERE title = 'An Unusual Start to The Summer' AND summary = 'This is a filler which I have stolen from a good story' AND usrID = '1')
                """
    )

    execute( 
                """
                INSERT INTO stories (title, summary, usrID)
                SELECT 'Pineapples are cool', 'random song lyrics as I continously fill this form out', '2'
                WHERE NOT EXISTS
                    (SELECT title, summary, usrID
                    FROM stories
                    WHERE title = 'Pineapples are cool' AND summary = 'random song lyrics as I continously fill this form out' AND usrID = '2')
                """
    )

    execute( 
                """
                INSERT INTO story_db (storyID, content, usrID)
                SELECT '2', 'Stirs of whispers trail and linger You still haunt the corners of my heart', '2'
                WHERE NOT EXISTS
                    (SELECT storyID, content, usrID
                    FROM story_db
                    WHERE storyID = '2' AND content = 'Stirs of whispers trail and linger You still haunt the corners of my heart' AND usrID = '2')
                """
    ) 

    execute( 
                """
                INSERT INTO story_db (storyID, content, usrID)
                SELECT '2', 'Singing me to sleep. Singing dont love the bottle but the bottle loves me. Sing it for me baby. Singing me to sleep. Singing dont love the bottle with a deeper disdain.', '1'
                WHERE NOT EXISTS
                    (SELECT storyID, content, usrID
                    FROM story_db
                    WHERE storyID = '2' AND content = 'Singing me to sleep. Singing dont love the bottle but the bottle loves me. Sing it for me baby. Singing me to sleep. Singing dont love the bottle with a deeper disdain.' AND usrID = '1')
                """
    ) 



    
        