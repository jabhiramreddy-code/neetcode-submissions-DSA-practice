class Account:
    def __init__(self, name, balance):
        self.title = name
        self._balance = balance
        pass
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")
        pass


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
