#people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

#filtered_object = filter(lambda s: len(s) <= 4, people)
#map_object = map(lambda s: print("Bonjour"+filtered_object),people)
#print(map_object)

class BankAccount:

  def __init__(self, account_number, balance=0):
    self.account_number = account_number
    self.balance = balance
    self.transactions = []

  def view_balance(self):
    self.transactions.append("View Balance")
    print(f"Balance for account {self.account_number}: {self.balance}")

  def deposit(self, amount):
    if amount <= 0:
      print("Invalid amount")
    elif amount < 100:
      print("Minimum deposit is 100")
    else:
      self.balance += amount
      self.transactions.append(f"Deposit: {amount}")
      print("Deposit Succcessful")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient Funds")
    else:
      self.balance -= amount
      self.transactions.append(f"Withdraw: {amount}")
      print("Withdraw Approved")
      return amount

  def view_transactions(self):
    print("Transactions:")
    print("-------------")
    for transaction in self.transactions:
      print(transaction)

newCount = BankAccount('BA0012', 1000000)
newCount.view_balance()
newCount.deposit(50000)
newCount.view_balance()
newCount.withdraw(2000)
newCount.view_balance()
newCount.view_transactions()
