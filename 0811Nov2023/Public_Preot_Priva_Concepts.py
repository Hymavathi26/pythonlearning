# #public---we can access directly
# #protect--Not access directly-we can access by creating public method internally and then call
# #private-Not access directly, through creating public method by using oublic function we can call
#
# class BankAccount:
#     def __init__(self):
#         self.balance=0
#
#     def deposite(self,amount):
#         self.balance+=amount
#
#     def _withdraw(self,amount):
#         self.balance-=amount
#
#     def __show_blc(self):
#         print("your balance is : ",self.balance)
#
#     def Is_auth_True_show_blc(self,Is_auth):     #create public function to access private methos
#         if Is_auth:
#             print(self.__show_blc())       #access private function
#         else:
#             print("you are not auth")
#
#
# accountDetails=BankAccount()
# accountDetails.deposite(1000)
#
#
# accountDetails._withdraw(500)   #Not a good practice
#
# #accountDetails.__show_blc()      #NOt able to access directely
#
# accountDetails.Is_auth_True_show_blc(True)           #returns the output value
# #accountDetails.Is_auth_True_show_blc(False)


#EX2: creteate a public function for access the protected method

class BankAccountDetails:

    def __init__(self):
        self.balance = 0
        #self.__private_var=200    #we can initialize the private and publuic values

    def Amount_deposite(self,amount):
        self.balance+=amount
        print("Total balace after deposited:",self.balance)

    def _amount_withdraw(self,amount):
        self.balance-=amount
        print("avaialble balance after withdraw:",self.balance)

    def __display_total_amount(self):
        print("check your balance :",self.balance)

    def IS_AUTH_TRUE_SHOW_BLC(self,IsAuth):     # Create public function
        if IsAuth:
            self.__display_total_amount()     #accss private method by using public function
        else:
            print("You are not auth")

    def do_withdraw_by_Bank_Manager(self,amount):   #create public function
        self._amount_withdraw()        #with in public function internally call the protected method


Bank_amount_details=BankAccountDetails()

Bank_amount_details.Amount_deposite(2000)

Bank_amount_details._amount_withdraw(1000)


Bank_amount_details.IS_AUTH_TRUE_SHOW_BLC(True)        #it return the remains available value 1000
#Bank_amount_details.IS_AUTH_TRUE_SHOW_BLC(False)       #return  "you not auth " as output

#Never use this process
Bank_amount_details._BankAccountDetails__private_var = 100
print(Bank_amount_details._BankAccountDetails__private_var) # Super Bad Pratice - Python allow this , Java
