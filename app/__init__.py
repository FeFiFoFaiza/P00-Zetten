from flask import Flask, render_template, request
from flask import session, redirect, url_for

from management import create_user, authenticate_user

app = Flask(__name__)    #create Flask object

database = {}

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
            username = session['username']
        )
    
    '''If not logged in go to guest page'''
    return render_template("guest_homepage.html")
        



""" def disp_loginpage():
    print(session)
    if 'username' in session: #checks if cookie is stored
        return render_template('response.html', username1= session['username']) #if stored, take to the response page
    return redirect(url_for('authenticate')) # if not stored, take to login page
 """

# Session clearing/Logout
# Honestly this is for me so I know that the guest page works
@app.route("/log-out", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return "test.html"


@app.route("/auth", methods = ['GET','POST'])
def authenticate():

    # GET request: display the form
    if request.method == "GET":
        return render_template("login.html")

    usr = request.form['username']
    psw = request.form['password']

    # The Log-In Worked!
    if authenticate_user(usr, psw):
        session["username"] = usr
        return render_template('homepage.html', username = usr)

    return render_template('login.html', result = "username or password is incorrect")


#create registration:

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if "username" in session:
        return redirect(url_for('index'))

    # GET request: display the form
    if request.method == "GET":
        return render_template("registration.html")

    # POST request: handle the form response and redirect
    username = request.form["username"]
    password = request.form["password"]
    
    create_user(username, password)

    return redirect(url_for('authenticate'))
    
@app.route("/registerauth", methods = ['GET', 'POST'])
def registerauth():
    if request.method == 'POST':
        print(request.form)
        print("SKJDHFKJDSHFDSFDSFFDS")
        if (request.form['username'] in database):
            print("IM IN UR WALLS")
            return render_template("registration.html", result = "username already exists")
        else:
            database[request.form['username']] = request.form['password']
            return redirect(url_for('authenticate'))



app.secret_key = 'girlboss'

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
