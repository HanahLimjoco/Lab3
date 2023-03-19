import pickle
import random

from bank import Bank
from savingsaccount import SavingsAccount

bank = Bank()

bank.add(SavingsAccount("Limjoco","1001",2500.00))
bank.add(SavingsAccount("Cristobal","1002",4000.00))
bank.add(SavingsAccount("Centeno","1003",3500.00))
bank.add(SavingsAccount("Kitagawa","1004",2000.00))
bank.add(SavingsAccount("Abella","1005",1000.00))

print(bank)
