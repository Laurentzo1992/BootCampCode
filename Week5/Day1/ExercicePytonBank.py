from datetime import datetime
from time import strptime


class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
        if balance > 0:
            self.deposit(balance, account_name, "Alice Ilboudo", "BCB Centre", datetime.strptime('14/01/2020', '%d/%m/%Y'))
    def view_balance(self, person, user, venue, amount=0, transaction_time=datetime.now()):
        self.transactions.append({'transaction_type': 'View Balance', 'transaction_time': transaction_time, 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
        print(f"Balance for account {self.account_number}: {self.balance}")
    def deposit(self, amount, person, user, venue, transaction_time=datetime.now()):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append({'transaction_type': 'Deposit', 'transaction_time': transaction_time, 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
            print("Deposit Succcessful")
    def withdraw(self, amount, person, user, venue, transaction_time=datetime.now()):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append({'transaction_type':'withdrawal', 'transaction_time': transaction_time, 'transaction_amount': amount, 'transaction_by': person, 'transaction_operator': user, 'transaction_venue': venue})
            print("Withdraw Approved")
            return amount
    def view_transactions(self):
        print("Transactions:")
        print("-------------\n\n\n")
        for transaction in self.transactions:
            print(transaction)
            print("\n---")


newCount = BankAccount("BA0012", "NIKIEMA Laurent", 10000000)
print("\n---")
newCount.view_balance("NIKIEMA Laurent", "TAPSOBA ALICE", "CORIS KWAME NKROUMA", datetime.strptime('14/02/2022', '%d/%m/%Y'))
print("\n---")
newCount.deposit(15000000,"SANKARA STEVE", "TAPSOBA ALICE", "CORIS KWAME NKROUMA", datetime.strptime('14/03/2022', '%d/%m/%Y'))
print("\n---")
newCount.view_balance("NIKIEMA Laurent", "TAPSOBA ALICE", "CORIS KWAME NKROUMA", datetime.strptime('14/04/2022', '%d/%m/%Y'))
print("\n---")
newCount.withdraw(10000000,"SANKARA STEVE", "TAPSOBA ALICE", "CORIS KWAME NKROUMA", datetime.strptime('14/05/2022', '%d/%m/%Y'))
print("\n---")
newCount.view_balance("NIKIEMA Laurent", "TAPSOBA ALICE", "CORIS KWAME NKROUMA", datetime.strptime('14/08/2022', '%d/%m/%Y'))
print("\n---")
# newCount.view_transactions()
transactions = newCount.transactions
print(f" Le nombre de transaction est : {len(transactions)}")
print("\n---")
print(transactions, "\n")
deposits = [deposit for deposit in transactions if deposit['transaction_type'] == 'Deposit']
retraits = [retrait for retrait in transactions if retrait['transaction_type'] == 'withdrawal']
print(f" Le nombre de depot est : {len(deposits)}")
print("\n---")
print(f" Le nombre de retrait est : {len(retraits)}")
credit = sum([deposit['transaction_amount'] for deposit in deposits])
debit = sum([retrait['transaction_amount'] for retrait in retraits])
print("\n---")
print(f"Totaux des depots actuel est : {credit}")
print("\n---")
print(f"Totaux des retraits  actuel est : {debit}")
print("\n---")
solde = credit-debit
print(f" votre sold est : {solde}")
#transaction antérieur à avril 2022

periodeAvril = [periode for periode in transactions if periode['transaction_time'] < datetime.strptime('01/04/2022', '%d/%m/%Y')]
print("\n---")
print(f"Le nombre de transaction antérieur à avril  2022 est : {len(periodeAvril)}")
