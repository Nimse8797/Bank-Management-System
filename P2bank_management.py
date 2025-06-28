class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number=account_number
        self. holder_name= holder_name
        self.balance=balance

    def deposit(self,amount):
     
        if amount>0.0:
            self.balance+=amount
            print(f"Rs{amount} deposited.New balance:Rs{self.balance}")
        
        else:
            print("Invalid amount deposited")

    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            print(f"{amount} withdrawn.Remaining Balance:{self.balance}")
        else:
            print("Insufficient Bank Balance")

    def disp_balance(self):
        print(f"account Hoder:{self.holder_name} | Balance:{self.balance}")

    def transfer(self,amount,target_account):
        if 0<amount<self.balance:
            self.balance-=amount
            print(f"{amount} transferred to {target_account}")
        else:
            print("Insufficient money for transaction")

class Savings_Acc(Account):
          def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.05):
              super().__init__ ( account_number, holder_name, balance)
              self.interest_rate =interest_rate

          def calculate_interest(self):
              interest=self.balance*self.interest_rate
              print(f"Interest is:{interest}")
              return interest
          

class Current_Acc(Account):
        def __init__(self,account_number, holder_name, balance=0.0, overdraft_limit=5000,overdraft_interest_rate=0.10):
            super().__init__(account_number, holder_name, balance)
            self.overdraft_limit=overdraft_limit
            self.overdraft_interest_rate = overdraft_interest_rate
            def deposit(self, amount):
                if amount > 0:
                   self.balance += amount
                   print(f"Rs{amount} deposited to Current Account. New balance: Rs{self.balance}")
                else:
                      print("Invalid deposit amount.")

        def withdraw(self,amount):
                if 0<amount<self.balance+self.overdraft_limit:
                    self.balance-=amount
                    print(f"{amount} withdrawn.Remaining Balance is:{self.balance}")
                    if self.balance<0:
                         self.apply_overdraft_interest_rate()
                else:
                    print("Cannot Withdraw money.Amount exceeded Balance")

        def apply_overdraft_interest_rate(self):
                 overdraft_amount = abs(self.balance)  
                 interest = overdraft_amount * self.overdraft_interest_rate
                 self.balance -= interest
                 print(f" Overdraft Interest of ₹{interest:.2f} applied on ₹{overdraft_amount}.")
                 print(f"Updated balance after interest: ₹{self.balance:.2f}")


if __name__ == "__main__":
        acc1 = Savings_Acc("S001", "Vaishnavi", 10000)
        acc2 = Current_Acc("C001", "nandini", 5000)
        acc1.disp_balance()
        acc1.deposit(5000)
        acc2.withdraw(10000)
        acc2.withdraw(8000)
        acc1.transfer(300,acc2)
        acc2.deposit(10000)