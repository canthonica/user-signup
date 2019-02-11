from flask import Flask, request, redirect, render_template
import re 
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    #username = request.args.get('username')
    #error = request.args.get("error")
    #pass_err = request.args.get("pass_err")
   # verify_err = request.args.get("verify_err")
    #email_err = request.args.get("email_err")
    #password = request.args.get('password')
    return render_template('add-user.html')

# Defines if string has characters
def has_char(chex):
    if chex != "":
        return True
    else:
        return False

def space(verify):
    whitespace = " "
    if whitespace not in verify:
        return True
    else:
        return False

#def email(validate):








@app.route("/user", methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error =  ""
    pass_err = ""
    verify_err = ""
    email_err = ""
    
    #user_sign = " "
       
    if not has_char(username):
        error = "Invalid Username"
        
    else:
        if len(username) < 4 or len(username)  > 20:
            error = "Invalid Username"

    if not has_char(password):
        pass_err = "Invalid Password. Please enter a password between 3 and 20 characters"
          
    else:
        if len(password) < 4 or len(password) > 20:
            pass_err = "Invalid Password. Please enter a password between 3 and 20 characters"
            
          
    if not has_char(verify):
        verify_err = "Please enter password"
        
    else:
        if password != verify:
            verify_err ="Please enter password"
            
    if has_char(email):
        if email != "":
            if "@" not in email:
                email_err = "Invalid Email"
            elif "." not in email:
                email_err = "Invalid Email"
            elif len(email) < 4 or len(email) > 20:
                    email_err = "Invalid Email"
            else:
                if " " in email:
                    email_err = "Invalid Email"

    if not error and not pass_err and not verify_err:
        #error = ""
        #pass_err = ""
        #verify_err = ""
       # email_err = ""
        
        return render_template('welcome.html', username=username)
    else:
        return render_template('add-user.html', username=username, email=email, error=error, pass_err=pass_err, verify_err=verify_err, email_err=email_err)
        
'''   
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
'''
               




if __name__ == "__main__":
    app.run()