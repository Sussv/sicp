"""Lab 6: OOP and Inheritance"""

import random

# ANSWER QUESTION q1

# ANSWER QUESTION q2

#####################
# Required Problems #
#####################


class PrintModule:
    def pp(self):
        pretty_print(self)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, product: str, price: int):
        """Set the product and its price, as well as other instance attributes."""
        self.product_name=product
        self.product_price=price
        self.product_quantity=0
        self.balance=0

    def restock(self, quantity: int) -> str:
        """Add quantity to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        assert quantity > 0
        self.product_quantity+=quantity
        return 'Current {0} stock: {1}'.format(self.product_name,self.product_quantity)

    def add_funds(self, funds: int) -> str:
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Machine is out of stock. Here is your $4.

        Otherwise, add funds to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        if self.product_quantity==0:
            return 'Machine is out of stock. Here is your ${0}.'.format(funds)
        else:
            self.balance+=funds
            return 'Current balance: ${0}'.format(self.balance)

    def vend(self) -> str:
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy.
        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Machine is out of stock.
        E.g., You must add $3 more funds.
        """
        if self.product_quantity>0:
            if self.balance==self.product_price:
                temp=self.balance
                self.balance=0
                self.product_quantity-=1
                return 'Here is your {0}.'.format(self.product_name)
            elif self.balance>self.product_price:
                temp=self.balance
                self.balance=0
                self.product_quantity-=1
                return 'Here is your {0} and ${1} change.'.format(self.product_name,temp-self.product_price)
            else:
                return 'You must add ${0} more funds.'.format(self.product_price-self.balance)
        else:
            return 'Machine is out of stock.'

class Pet(PrintModule):
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """

    def __init__(self, name, owner):
        self.is_alive = True  # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

    def to_str(self):
        return '({0}, {1})'.format(self.name,self.owner)


class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives=lives

    def talk(self):
        """Print out a cat's greeting."""
        print('{0} says meow!'.format(self.name))

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print(f"{self.name} has no more lives to lose.")
        else:
            self.lives-=1
            if self.lives==0:
                self.is_alive=False

    def to_str(self):
        return '({0}, {1}, {2})'.format(self.name,self.owner,self.lives)


class NoisyCat(Cat):  # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    def talk(self):
        """Talks twice as much as a regular cat."""
        super().talk()
        super().talk()

class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[34m"
    OKCYAN = "\033[35m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def pretty_print(obj):
    """Pretty prints the object using the Colors class.
    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> pretty_print(kyubey)
    \033[34mPet\033[0m\033[35m(Kyubey, Incubator)\033[0m
    """
    class_name=type(obj).__name__
    content=obj.to_str()
    print(f"{Colors.OKBLUE}{class_name}{Colors.ENDC}{Colors.OKCYAN}{content}{Colors.ENDC}")