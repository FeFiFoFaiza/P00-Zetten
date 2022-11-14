""" THIS WILL HANDLE UPDATING A STORY """

from cheats import execute
from management import User
from story_db import StoryDB

class Story:

    def __init__(self, id):

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

        data = execute('SELECT * FROM `stories` WHERE `stories`.storyID=%d' % int(id)).fetchall()
        assert (len(data) != 0)

        updates = execute('SELECT usrID FROM `story_db` WHERE `story_db`.id=%d' % int(id)).fetchall()
        assert (len(data) != 0)

        self.id = data[0][0]
        self.title = data[0][1]
        self.summary = data[0][2]
        self.authors = User(data[0][3])

        self.updates = list()  # ids of all the users who added to the story
        for a in updates:
            self.updates.append(a[0])

    def get_updates(self):

        updates = execute('SELECT id FROM `story_db` WHERE storyID=%d' % int(self.id)).fetchall()

        l = list()
        for update in updates:
            l.append(StoryDB(update[0]))

        l.append("Yikes baby")

        return l

    @staticmethod
    def new_story(user, title, summary, content):
        execute( 'INSERT INTO `stories` (title, summary, usrID) VALUES ("%s", "%s", %d);' % (title, summary, user.id) )

        story_id = int(execute('SELECT storyID FROM `stories` ORDER BY storyID DESC LIMIT 1').fetchall()[0][0])

        StoryDB.new_update(Story(story_id), content, user)

        return story_id
