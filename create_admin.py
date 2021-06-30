from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input('Input your name: ')

    if User.query.filter(User.username == username).count():
        print('This username is already taken')
        sys.exit(0)

    password1 = getpass('Enter your password : ')
    password2 = getpass('Repeat the password : ')

    if not password1 == password2:
        print("Passwords aren't the same")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('User is authenticated with the id={}'.format(new_user.id))