from flask import Flask
from flask_restful import Api

from resources.user import User, UserList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
