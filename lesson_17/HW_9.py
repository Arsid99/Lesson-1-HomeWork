from unittest import TestCase
from datetime import datetime
from uuid import uuid4, UUID
from lesson_12 import bank_client_class


class BankAccountTestCase(TestCase):
    def setUp(self):
        self.now = datetime.now().date()
        self.name = "Sydorenko R.M."
        self.deposit_sum = 2402
        self.withdrawal_sum = 2022
        self.account_number = uuid4()
        self.create_acc = bank_client_class.BankClient(self.name, self.account_number)

    def test_name_and_uuid(self):
        self.assertEqual(self.create_acc.account_name, 'Sydorenko R.M.')
        self.assertTrue(self.create_acc.unique_id, UUID)

    def test_all_transactions(self):
        self.create_acc.deposit_of_funds(self.deposit_sum)
        self.create_acc.withdrawals_of_funds(self.withdrawal_sum)
        self.assertEqual(len(self.create_acc.transactions), 2)

    def test_balance(self):
        self.create_acc.deposit_of_funds(self.deposit_sum)
        self.create_acc.withdrawals_of_funds(self.withdrawal_sum)
        self.assertEqual(self.create_acc.obtaining_a_balance(),
                         "Sydorenko R.M., your balance is 359.78, after these transactions:"
                         "[['On 2022-11-02 you deposited 2402$ into your bank account'],"
                         " ['2022-11-02 you withdrew 2022$ from your bank account']]")

    def test_name(self):
        self.assertIsInstance(self.create_acc.account_name, str)

    def test_uuid(self):
        self.assertIsInstance(self.create_acc.unique_id, UUID)

    def test_account(self):
        self.assertIsInstance(self.create_acc, bank_client_class.BankClient)
