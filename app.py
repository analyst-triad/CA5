from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'
  
# Database configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'user_data'
}


# Function to check if a user exists
def user_exists(username):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result is not None
    finally:
        cursor.close()
        connection.close()
        
@app.route('/')
def index() -> str:
    return "Welcome to site"

# Sign-up route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if user_exists(username):
            flash('Username already exists. Please choose a different username.', 'danger')
        else:
            try:
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                connection.commit()
                flash('Sign-up successful. You can now log in.', 'success')
            finally:
                cursor.close()
                connection.close()
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()

            if result:
                flash('Login successful!', 'success')
            else:
                flash('Login failed. Please check your username and password.', 'danger')
        finally:
            cursor.close()
            connection.close()
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
