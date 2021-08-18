from . import load_json

class Authentication:
    def __init__(self, database="data\\data_main.json", username=None, password=None)-> None:
        self.username = None
        self.password = None
        self.data = load_json.load(database)
        
        self.users = self.data["users"]

        self.user_info = None


    def login(self, typed=False, username=None, password=None):
        if (typed):
            self.username = input("Type username: ")
            self.password = input("Type password: ")
        else:
            self.username = username
            self.password = password

        try:
            if self.users[self.username]["password"] == self.password: 
                self.user_info = self.users[self.username]
                print(f"Logged in as {self.username}")
                return self.user_info # Returns the user info as a dictionary


            else: 
                print("Incorrect username or password")
        except: 
            print("Incorrect username or pasword")