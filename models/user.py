from sqlalchemy import Column, Integer, String
from models.database import Database
from getpass import getpass

BASE = Database.getBase()

class User(BASE):
   __tablename__ = "Users"
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String(50), nullable=False)
   email = Column(String(200), nullable=False, unique=True)
   password = Column(String(250), nullable=False)
   
   @classmethod
   def getUserCredentials(cls):
      name = input("Type your name: ").strip()
      email = input("Type your email: ").strip()
      password = getpass("Type your password: ").strip()
      user = User(name=name, email=email, password=password)
      
      return user
   
BASE.metadata.create_all(Database.engine)