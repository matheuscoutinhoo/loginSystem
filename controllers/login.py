from models.database import Database
from models.user import User
from getpass import getpass
from time import sleep

session = Database.createSession()

class LoginController():
   @classmethod
   def getLoginCredentials(cls):
      email = input("Please, type your email: ")
      password = getpass("Please, type your password: ")
      
      user = {"email": email, "password": password}
      return user
   
   @classmethod
   def verifyUser(cls, user):
      try:
         verifiedUser = session.query(User).filter_by(email=user["email"], password=user["password"]).one()
         if verifiedUser:
            return True, verifiedUser
         
         print("This account was not found!")
         sleep(3)
         return False
      except Exception as e:
         print(f"\nAn error occurred while attempting to validate user. {e}")
   