from controllers.register import RegisterController
from controllers.login import LoginController
from models.user import User
from time import sleep
import os

def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')

def main():
   while True:
      clear_screen()
      print("Welcome to login center!\n\nPlease select an option:\n")
      try:
         option = int(input("1 - Create account\n2 - Make login\n3 - Exit\nOption: ").strip())
         
         if option == 1:
            clear_screen()
            newUser = User.getUserCredentials()
               
            if RegisterController.register(newUser):
               print("\nUSER WAS SUCCESSFULLY REGISTERED!")
               sleep(2)
            else:
               print("\nRegistration failed. Please try again.")
               sleep(200)
         elif option == 2:
            clear_screen()
            user = LoginController.getLoginCredentials()
            _, loggedUser = LoginController.verifyUser(user)
            if loggedUser:
               clear_screen()
               print(f"THE USER WAS SUCCESSFULLY LOGGED IN!\nHello {loggedUser.name}")
            sleep(5)
         elif option == 3:
            clear_screen()
            print("Thank you for using our system!")
            break
         else:
            print("\nInvalid option. Please try again.")
            sleep(2)
      except ValueError:
         print("\nPlease enter a valid number!")
         sleep(2)
         continue


if __name__ == "__main__":
   main()