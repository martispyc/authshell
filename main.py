import json

class Base:
    def __init__(self, username, password, database) -> None:
        self.username = username
        self.password = password
        
        self.newlines_before_command = 0
        self.user_info = None
        with open(database) as f: self.users = json.load(f)["users"]

    def login(self, input=False):
        if (input):
            self.username = input("Type username: ")
            self.password = input("Type password: ")

        try:
            self.user_info = self.users[self.username][0]
            if self.user_info["password"] == self.password: 
                print(f"Logged in as {self.username}")
                self.username = self.username
                self.newlines_before_command = self.user_info["newlines_before_command"]

            else: print("Incorrect username or password")
        except: print("Incorrect username or pasword")


    def console(self):
        print(f"\n\nHello {self.username}, type '-register' to get started, or if you already are a user, type '-login'\n")
        self.login()
        while c:= input(self.newlines_before_command * ('\n')+"> "):
            if (c == "-login"): self.login(input=True)

            elif (c == "set -newlines"): self.newlines_before_command = int(input("amount: "))


if __name__ == "__main__":
    Base(
        username="martis",
        password="qwerty", 
        database="data1.json"
    ).console()