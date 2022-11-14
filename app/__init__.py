import os

from flask import Flask, render_template, request
from flask import session, redirect, url_for

import cheats
from management import User
from story import Story
from currentUser import currentUser

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
cheats.setup() 
#FUTURE PLANS MAKE SURE TO CHECK IF FORMS ARE VALID


#The Landing Site'
@app.route("/")
@app.route("/index")
def index():
    if 'username' in session:

        '''Get the user id'''

        '''Get the stories they've contributed to via user id
            preferably in a certain type of format (probs make sep method for this)'''

        return render_template(
            "homepage.html",
            username = session['username'],
            currUsrSess = currentUser(session['user_id'])
        )
    
    '''If not logged in redirected to guest page'''
    return render_template("landing_site.html")
        

# Session clearing/Logout
# Honestly this is for me so I know that the guest page works
@app.route("/log-out", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return "error.html"


@app.route("/login", methods = ['GET','POST'])
def login():

    # GET request: display the form
    if request.method == "GET":
        return render_template("login.html")

    usr = request.form['username']
    psw = request.form['password']

    # The Log-In Worked!
    if User.authenticate_user(usr, psw):
        session["username"] = usr
        session["user_id"] = User.get_ID(usr)
        return render_template('homepage.html', username = usr, currUsrSess = currentUser(session["user_id"]))

    return render_template('login.html', result = "username or password is incorrect")


#create a new account:
@app.route("/register", methods = ['GET', 'POST'])
def register():

    if "username" in session:
        return redirect(url_for('index'))

    # GET request: display the form
    if request.method == "GET":
        return render_template("registration.html")

    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']
    
    User.new_user(username, password)

    return redirect(url_for('login'))

#~~~~~~~~~~~~~~~STORY STUFF~~~~~~~~~~~~~~~~

#displays all stories
@app.route("/stories")
def stories():
    return render_template("error.html") # a place holder

#view a specific story
@app.route("/stories/<id>", methods=['GET', 'POST'])
def showStory(id):
    story = Story(id)

    return render_template('story.html', to_render = story)


#create a new story
@app.route("/stories/new", methods = ['GET', 'POST'])
def newStory():

    # If the user is not logged in
    if "username" not in session:
        return redirect(url_for('login'))
    
    if request.method == "GET":
        return render_template("new_story.html")

    title = request.form['title']
    summary = request.form['summary']
    content = request.form['content']

    newStory_id = Story.new_story(User(session["user_id"]), title, summary, content)
    newS = Story(newStory_id)
    
    return redirect(f'/stories/{newStory_id}')




if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
