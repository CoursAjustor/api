from flask import jsonify
from services.UserService import UserService

class UsersController(object):
  @staticmethod
  def getAll():
    return jsonify(UserService.getAll())
    
