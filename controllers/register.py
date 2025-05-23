from models.database import Database
from models.user import User
from getpass import getpass
from time import sleep
from hashlib import sha256


session = Database.createSession()

class RegisterController:
   
   @classmethod
   def validate(cls, name, email, password):
      if len(name) < 3 or len(name) > 50:
         return False
      if len(email) < 5 or len(email) > 200:
         return False
      if len(password) < 6 or len(password) > 100:
         return False
      
      try:
         user = session.query(User).filter_by(email=email).all()
         if user:
            print("\nThis user already exists!")
            return False
         
         return True
      except Exception as e:
         print(f"\nAn error occurred while attempting to validate user. {e}")
   
   @classmethod
   def register(cls, user: User):
      if not cls.validate(user.name, user.email, user.password):
         print("\nSome of your credentials are not valid, please type it again!")
         sleep(5)
         return False    
      try:
         user.password = sha256(user.password.encode()).hexdigest()
         session.add(user) 
         session.commit()
         session.close()
         return True
      except Exception as e:
         print(f"Error while trying to register user in database. {e}")
   