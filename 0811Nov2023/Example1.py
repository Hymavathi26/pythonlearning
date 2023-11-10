# # #To print length of pwd by using private method
class password:

    def __init__(self,password):
        self.__password=password

    def print_len(self):          #create public function to access __private method
        print("your password length is :",len(self.__password))

pwd=password("hyma123")
pwd.print_len()                   #print length of password

#EX2:print len of pwd with condition and using get and set method

class Password:
    def __init__(self,password):
        self.__password=password
        print("length of pwd is ",len(self.__password))

    def print_pwd(self,pwd):
        if len(pwd) > 10:
            print((pwd))
        else:
            print("week password")

PWD=Password("hyma")      #it calls constructor methos and print    #length of pwd is  4
PWD.print_pwd("hyma12")     #condition is applied here only    #  week password--becoze len is less than 10
PWD.print_pwd("hymavathi1234567")       #condition is applied here it print   #hymavathi1234567

