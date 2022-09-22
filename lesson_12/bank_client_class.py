from decimal import Decimal
from uuid import uuid4, UUID
from datetime import datetime as dt


class BankClient:
    def __init__(self, account_name: str, unique_id: UUID):
        self.account_name = account_name
        self.unique_id = unique_id
        self.balance = Decimal('0')
        self.transactions = []

    def deposit_of_funds(self, amount: float):
        deposit_list = []
        current_time = dt.now().strftime('%Y-%m-%d')
        self.balance += Decimal(str(amount))
        deposit_list.append(f'On {current_time} you deposited {amount}$ into your bank account')
        self.transactions.append(deposit_list)

    def withdrawals_of_funds(self, amount: float):
        withdrawals_list = []
        current_time = dt.now().strftime('%Y-%m-%d')
        self.balance -= Decimal(str(amount + (amount * 0.01)))
        withdrawals_list.append(f'{current_time} you withdrew {amount}$ from your bank account')
        self.transactions.append(withdrawals_list)

    def obtaining_a_balance(self):
        return f"{self.account_name}, your balance is {self.balance.quantize(Decimal('0.00'))}," \
               f" after these transactions:\n{bank_client.transactions}"


bank_client = BankClient('"client_name"', uuid4())
print(bank_client.account_name, bank_client.unique_id)
bank_client.deposit_of_funds(1000)
bank_client.withdrawals_of_funds(581)
bank_client.deposit_of_funds(523)
bank_client.withdrawals_of_funds(515)
bank_client.deposit_of_funds(1451)
bank_client.withdrawals_of_funds(785)
print(bank_client.obtaining_a_balance())
