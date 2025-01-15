"""
Test Cases TestAccountModel
"""
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError
from factories import AccountFactory

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_accounts(self):
        """ Test creating multiple Accounts """
        for _ in range(10):
            account = AccountFactory()
            account.create()
        self.assertEqual(len(Account.all()), 10)

    def test_create_an_account(self):
        """ Test Account creation using known data """
        account = AccountFactory()  # Create a single account using AccountFactory
        account.create()
        self.assertEqual(len(Account.all()), 1)

    def test_repr(self):
        """Test the representation of an account"""
        account = AccountFactory(name="Foo")  # Use AccountFactory to create an account
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """ Test account to dict """
        account = AccountFactory()  # Create an account using AccountFactory
        result = account.to_dict()
        self.assertEqual(account.name, result["name"])
        self.assertEqual(account.email, result["email"])
        self.assertEqual(account.phone_number, result["phone_number"])
        self.assertEqual(account.disabled, result["disabled"])
        self.assertEqual(account.date_joined, result["date_joined"])

    def test_from_dict(self):
        """ Test account from dict """
        account = AccountFactory()  # Create an account using AccountFactory
        data = account.to_dict()  # Convert the account to a dict
        new_account = AccountFactory()  # Create a new Account instance
        new_account.from_dict(data)  # Populate it using the dict
        self.assertEqual(new_account.name, data["name"])
        self.assertEqual(new_account.email, data["email"])
        self.assertEqual(new_account.phone_number, data["phone_number"])
        self.assertEqual(new_account.disabled, data["disabled"])

    def test_update_an_account(self):
        """ Test Account update using known data """
        account = AccountFactory()  # Create an account using AccountFactory
        account.create()
        self.assertIsNotNone(account.id)
        account.name = "Rumpelstiltskin"
        account.update()
        found = Account.find(account.id)
        self.assertEqual(found.name, account.name)

    def test_invalid_id_on_update(self):
        """ Test invalid ID update """
        account = AccountFactory()  # Create an account using AccountFactory
        account.id = None
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """ Test Account delete using known data """
        account = AccountFactory()  # Create an account using AccountFactory
        account.create()
        self.assertEqual(len(Account.all()), 1)
        account.delete()
        self.assertEqual(len(Account.all()), 0)

