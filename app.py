from flask import Flask, request
import bcrypt

app = Flask(_name_)

@app.route('/register', methods=['POST'])
def register():
    password = request.form['password']
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return "Password stored securely!"

app.run()