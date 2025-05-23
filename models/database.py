from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

class Database():
   try:
      USER = ''
      PASSWORD = ''
      HOST = 'localhost'
      PORT = '5432'
      DATABASE = ''
      DB_PATH = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
      engine = create_engine(DB_PATH, echo=True)
      Session = sessionmaker(bind=engine)
      Base = declarative_base()
   except Exception as e:
      print(f"Error while connecting to Database: {e}")
   
   @classmethod
   def createSession(cls):
      return cls.Session()

   
   @classmethod
   def getBase(cls):
      return cls.Base
   

   
   