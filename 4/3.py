#TODO: add currency mode to rials
class NotValidAccount(Exception):
    e = 'Not Valid Account'

    def __str__(self):
        return self.e

class FloorBalanceError(Exception):
    def __init__(self, least):
        self.least = least

    def __str__(self):
        return f'You have to at least have {self.least} Rial in your account'

class BankAccount:
    ''' class for bank accounts.
        
        Args:
            name (str): name of the guy who owns this account.

            balance (int): balance of the account.

        Attributes:
            least_balance (int): the least balance that you cant have balance less than that in your account.

            __name (str): read-only attribute of owners name.

            __balance (int): balance of the account.
    '''
    __least_balance = 5000

    def __init__(self, name: str, balance: int):
        self.__name = name
        
        if balance < self.__least_balance:
            raise FloorBalanceError(BankAccount.__least_balance)
        else:
            self.__balance = balance
    
    def transfer(self, account, amount):
        ''' A function to transfer money from an account to another.
            
            Args:
                account (BankAccount): the destination bank account to transfer to.

                amount (int): the amount of money to transfer.

            Returns:
                success (bool): returns true in case the transaction in completed correctly.
             '''
        if isinstance(account, BankAccount) and self.__transaction_allowed(amount):
            self.__balance -= amount
            account.put(amount)

            print(f'{amount} rials transfered to {account.name}\'s account. Your balance: {self.balance}')

        else:
            raise NotValidAccount

    def take(self, amount):
        ''' A function to take the money.
            
            Args:
                amount (int): amount of money to take.

            
            '''
        if amount:
            if self.__transaction_allowed(amount):
                self.__balance -= amount

                print(f'{amount} Rial is taken from your account! Your balance: {self.balance}')
            else:
                raise FloorBalanceError(BankAccount.__least_balance)

    def put(self, amount):
        self.__balance += amount
        print(f'{amount} Rial was added to your account! Your balance: {self.balance}')

    @property
    def balance(self):
        return self.__balance

    def __transaction_allowed(self, amount):
        return self.__balance - amount >= self.__least_balance

    @property
    def name(self):
        return self.__name

roni = BankAccount('Roni', 40000)
rodrik = BankAccount('Rodrik', 40000)

roni.transfer(rodrik, 30000)
roni.take(5000)

rodrik.take(70000)