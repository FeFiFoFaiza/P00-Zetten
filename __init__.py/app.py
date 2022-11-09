from flask import Flask, render_template, request
from flask import session, redirect, url_for


app = Flask(__name__)    #create Flask object

database = {}

@app.route("/", methods = ['GET', 'POST'])
def disp_loginpage():
    print(session)
    if 'username' in session: #checks if cookie is stored
        return render_template('response.html', username1= session['username']) #if stored, take to the response page
    return redirect(url_for('authenticate')) # if not stored, take to login page


@app.route("/auth", methods = ['GET', 'POST'])
def authenticate():
    if 'username' in session:
        return redirect(url_for('disp_loginpage'))
    # if there is cookie, redirect this to response page
    if request.method == 'POST':
        if (request.form['username'] in database):
            if (database[request.form['username']] == request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('disp_loginpage'))  #response to a form submission
        else:
            return render_template('login.html', result = "username or password is incorrect")
    return render_template('login.html')


#create registration:

@app.route("/register", methods = ['GET', 'POST'])
def register():
    return render_template("registration.html", result = "")
    
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

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('authenticate'))
    else: 
        return redirect(url_for('disp_loginpage'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
