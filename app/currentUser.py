""" I have to make this to avoid circular importation :/ """

from management import User
from cheats import execute
from story import Story

class currentUser:
    
    def __init__(self, id):
        clone = User(id)
        self.id = clone.id
        self.username = clone.username
        self.password = clone.password

    def get_stories(self):

        data = execute('SELECT * FROM `stories` WHERE `stories`.usrID=%d' % self.id).fetchall()
        
        if len(data) == 0:
            return None

        stories = list()
        for s in data:
            stories.append(Story(s[0]))

        return stories

    def get_contributions(self):

        data = execute('SELECT storyID FROM `story_db` WHERE `story_db`.usrID=%d' % self.id).fetchall()
        if len(data) == 0:
            return None

        stories = list()
        for s in data:
            stories.append(Story(s[0]))
            
        return stories