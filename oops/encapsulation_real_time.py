class BankAccount:

    def __init__(self, account_number, initial_balance):
        
        self.__account_number = account_number
        self.__balance = initial_balance


    def deposit(self,amount):

        if amount >0 :
            self.__balance += amount
        return self.__balance
    def withdraw(self,amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    
    def get_balance(self):
        return self.__balance



    def get_account_number(self):
        return self.__account_number
    

obj = BankAccount(12345678,100)

print(obj.deposit(1233))


obj.withdraw(1500)


