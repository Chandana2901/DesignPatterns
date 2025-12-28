# using an interface to get a simplified version of complex logic
# there are mulitple classes 
# 1 for adding to db, 1 to validate username and password
# 1 to hash the password
# 1 to send the email to the user
# instead of creating relations between each and every class
# create 1 class that contains objects of all these classes
# add will call only the required functionalities when required


class Validator:
    def validate(self, username, password):
        if not username or not password:
            print("No username or password passed")

class PasswordHash:
    def hash(self, password):
        return f"hash_{password}"

class Email:
    def send(self, username):
        print(f"Welcome user {username} !! Registration successfull" )

class DBUpdate:
    def update(self, username, password):
        print(f"Added user : {username} to db")

class UserFacade:
    def __init__(self):
        self.validate = Validator()
        self.hash = PasswordHash()
        self.email = Email()
        self.dbUpdate = DBUpdate()
    
    def register(self, username, password):
        self.validate.validate(username, password)
        pwd = self.hash.hash(password)
        self.dbUpdate.update(username, pwd)
        self.email.send(username)


user = UserFacade()
user.register('abcdef', '123456789')        

