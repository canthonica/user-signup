from flask import Flask, request, redirect, render_template
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/user", methods=['POST'])
def signup():
    username = request.form['username']
    error = "Invalid Usernme. Please enter username between 3 and 20 characters"
    if len(username) < 3 or len(username) > 20:
        
        return redirect("/?error=" + error)
    
    else:
        
        return render_template("add-user.html", username=username )

@app.route("/password", methods=['POST'])
def passwords():
    password1 = request.form['password']
    if len(password1) < 3 or len(password1) > 20:
        error = "Invalid Password Please enter password between 3 and 20 characters"
        return redirect("/?error=" + error)

    else:
        return render_template("add-user.html", password=password1)





@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('add-user.html', error=error)


if __name__ == "__main__":
    app.run()


