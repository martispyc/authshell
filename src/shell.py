import json
from . import authentication

class Base:
    def __init__(self, username="", password="", database_path=""):
        self.username = username
        self.password = password

        self.database_path = database_path
        self.user_info = { # Default arguments
            "newlines_before_command": 0
        }

        self.authentication = authentication.Authentication(database=self.database_path)

        # Default arguments

        self.user_info = self.authentication.login(username=self.username, password=self.password)



    def console(self):
        print(f"\n\nHello {self.username}, type '-register' to get started, or if you already are a user, type '-login'\n")


        while c:= input(self.user_info["newlines_before_command"] * ('\n')+"> "):
            
            if (c == "end"): break

            elif (c == "-login"): 
                if self.authentication.login(typed=True) != None:
                    self.user_info = self.authentication.login(typed=True)

            elif (c == "set -newlines"): self.user_info["newlines_before_command"] = int(input("amount: "))

            else: print("Invalid command!")
