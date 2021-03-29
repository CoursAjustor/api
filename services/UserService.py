from models.UserModel import User

class UserService(object):
  @staticmethod
  def getAll():
    return [user.to_dict() for user in User.query.all()]