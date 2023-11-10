# #Use getter and setter with necessary conditions
#
class Password:
    def __init__(self,password):
        self.__password=password
        self.public_var=10

    def get_password(self,is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_pwd(self,password):
        if len(password) >10:
            self.__password=password
        else:
            print("week password:",len(password))

    def print_details(self):
        print("your pwd length is :",len(self.__password))

PASSWORD=Password("hyma123")
PASSWORD.print_details()

pssd=PASSWORD.get_password("False")
print(pssd)


PASSWORD.set_pwd("hymvathi1223456")

PASSWORD.print_details()



