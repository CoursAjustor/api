from flask import jsonify

class UsersController(object):
  @staticmethod
  def getAll():
    return jsonify([{"id": 1, "name": "plop"}])
    
