from app import app
from controllers.users.UsersController import UsersController

@app.route('/users', methods=['GET'])
def index():
    return UsersController.getAll()
