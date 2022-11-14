""" This will have creation and checking access to the database 
    THIS MAKES USER CLASS TO EASILY IDENTIFY USER IN DATABASE """

from cheats import execute
class User:

    def __init__(self, id):

        data = execute('SELECT * FROM `users` WHERE `users`.id=%d' % id).fetchall()
        assert (len(data) != 0)
        self.id = int(data[0][0])
        self.username = data[0][1]
        self.password = data[0][2]

    @staticmethod
    def new_user(username, password):

        # NOTE TO FUTURE SELF PLANS:
        # PUT IN SOME TYPE OF HASHCODE
        # ADD IN PARAMETERS FOR PASS AND USERNAME SIZE
        # MAYBE ID FOR STORIES?

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
                'INSERT INTO users(username, password) VALUES (\"%s\", \"%s\")' % (username, password)
            )

        return True


    def authenticate_user(username, password):

        user_pw = execute(
                'SELECT password FROM `users` WHERE `users`.username = \"%s\"' % username
            ).fetchone()

        if user_pw is not None:
            print(user_pw[0])
            return user_pw[0] == password

        return False

    def get_ID(username):

        return execute(
                'SELECT id FROM `users` WHERE `users`.username = \"%s\"' % username
            ).fetchone()
