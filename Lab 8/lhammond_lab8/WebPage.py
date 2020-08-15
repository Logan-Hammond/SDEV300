# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  WebPage.py
# Description:  Creates a simple webpage using Flask on an AWS Cloud9 instance.
#               Webpage allows user to create a new account, login, or update
#               the password for a given account. 
# IDE:			AWS Cloud9

import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__, static_url_path="/static")
limiter = Limiter(app, key_func=get_remote_address)

common_passwords = []
accounts = []

# Main page. 
@app.route("/hello", methods=["GET", "POST"])
def hello():
    return render_template("index.html")

# Submit pages. 
@app.route("/login", methods=["POST"])
@limiter.limit("15 per 2 minutes")
def login():
    reason_str = ""
    
    # Refresh and load account list in case it has been updated. 
    accounts = []
    with open("Lab8/accounts.csv", "r") as f: 
        reader = csv.reader(f, delimiter=",")
        for line in reader: 
            accounts.append(line)
            
    # Get data from form
    username = request.form["username"]
    password = request.form["password"]
    user_combo = [username, password]

    # Search for user in account list. 
    if user_combo not in accounts:
        reason_str = "Account not found."
    
    # Return failure page is reason_str is not empty. Otherwise return confirm. 
    if reason_str:
        # If login failed append instance of failure to log file. 
        with open("Lab8/log.txt", "a+") as lf:
            log_line = "{}\t{}\n".format(datetime.now(), request.remote_addr)
            lf.write(log_line)
        
        return render_template("signup_fail.html", reason = reason_str)
    return render_template("login_confirm.html")

@app.route("/signup", methods=["POST"])
def signup():
    reason_str = ""
    
    # Get data from form. 
    username = request.form["username"]
    password = request.form["password"]
    cpass    = request.form["cpass"]
    
    # Verify username is not already taken. 
    for a in accounts:
        if username == a[0]:
            reason_str = "Username is already taken."
    
    # Verify password is valid. 
    for word in common_passwords:
        if password == word[0]:
            reason_str = "Invalid password. Password is too common."
    if len(password) < 8:
        reason_str = "Invalid password. Password must be 8 or more characters."
    elif len(password) > 64:
        reason_str = "Invalid password. Password must be 64 or less characters."
    
    # Verify password is same as confirmation password. 
    if password != cpass:
        reason_str = "Password and confirmation password did not match."
    
    # Return failure page is reason_str is not empty.
    if reason_str:
        return render_template("signup_fail.html", reason = reason_str)
    
    # Add username and password to accounts and update account file. 
    account = [username, password]
    accounts.append(account)
    with open("Lab8/accounts.csv", "w") as af:
        for account in accounts: 
            new_row = "{},{}".format(account[0], account[1])
            af.write("{}\n".format(new_row))
    
    return render_template("signup_confirm.html")
    
@app.route("/update", methods=["POST"])
@limiter.limit("15 per 2 minutes")
def update():
    reason_str = ""
    
    # Load account list.  
    with open("Lab8/accounts.csv", "r") as f: 
        reader = csv.reader(f, delimiter=",")
        for line in reader: 
            accounts.append(line)
            
    # Get data from form. 
    username = request.form["username"]
    password = request.form["password"]
    cpass    = request.form["cpass"]
    
    # Verify account with username exists. 
    acc_exists = False
    for account in accounts:
        if username == account[0]:
            acc_exists = True
    if acc_exists == False:
        reason_str = "No account with that username found."
    
    # Verify password is valid. 
    for word in common_passwords:
        if password == word[0]:
            reason_str = "Invalid password. Password is too common."
    if len(password) < 8:
        reason_str = "Invalid password. Password must be 8 or more characters."
    elif len(password) > 64:
        reason_str = "Invalid password. Password must be 64 or less characters."
    
    # Verify password is same as confirmation password. 
    if password != cpass:
        reason_str = "Password and confirmation password did not match."
    
    # Return failure page is reason_str is not empty.
    if reason_str:
        return render_template("update_fail.html", reason = reason_str)
    
    # Get index of list in accounts
    index_num = 0
    for account in accounts:
        if account[0] == username:
            index_num = accounts.index(account)
    
    # Update password of account. 
    accounts[index_num][1] = password
    
    # Update accounts file. 
    with open("Lab8/accounts.csv", "w") as af:
        for account in accounts: 
            new_row = "{},{}".format(account[0], account[1])
            af.write("{}\n".format(new_row))
    
    # Return failure page is reason_str is not empty. Otherwise return confirm. 
    if reason_str:
        return render_template("signup_fail.html", reason = reason_str)
    return render_template("update_confirm.html")
    
# Confirmation pages.
@app.route("/loginconfirm", methods=["GET"])
def loginconfirm():
    return render_template("login_confirm.html")
    
@app.route("/signupconfirm", methods=["GET"])
def signupconfirm():
    return render_template("signup_confirm.html")
    
@app.route("/updateconfirm", methods=["GET"])
def updateconfirm():
    return render_template("update_confirm.html")

def main():
    # Create master account list and log files if they do not exist.  
    af = open("Lab8/accounts.csv", "a+")
    af.close() 
    lf = open("Lab8/log.txt", "a+")
    lf.close()
    
    # Load data from file. 
    with open("Lab8/CommonPassword.txt", "r") as f:
        for line in f.readlines():
            common_passwords.append(line.rsplit())
    
    # Run site. 
    app.run(host="0.0.0.0", port=8080)
    
if __name__ == "__main__":
    main()