class UserAccount:
    def __init__(self, username, email, password):
        self.username = username     
        self.email = email    
        self.__password = password        

    def set_password(self, __new_password):
        self.__password = __new_password
    
    def check_password(self,password):
        return self.__password == password

user = UserAccount(username="aboba", email="aboba2199@gmail", password="12345")
print(user.check_password("12345"))

user.set_password("54321")

print(user.check_password("54321"))
print(user.check_password("12345"))