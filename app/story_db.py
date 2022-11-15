""" THIS HANDLES ADDING TO A STORY INTO DATABASE """
from cheats import execute
from management import User

class StoryDB:

    def __init__(self, id):

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

        data = execute('SELECT * FROM `story_db` WHERE `story_db`.id=%d' % int(id)).fetchall()
        assert (len(data) != 0)

        self.id = data[0][0]
        self.storyID = data[0][1]
        self.content = data[0][2]
        self.usrID = data[0][3]

    @staticmethod
    def new_update(story, content, user):

        content = content.replace('"',r'""')

        execute( 'INSERT INTO `story_db` (storyID, content, usrID) VALUES (\"%s\", \"%s\", \"%s\")' % (story.id, content, user.id) )
