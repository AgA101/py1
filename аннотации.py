class Account:
    amount: int
    def __init__(self,amount: int):
        self.amount = amount

def fun(a : int,b : int) -> None:
    return a * b


a  : int = 6
print(a)
a = "Hello"
print(a)
print(fun(3,5.3))
mike = Account(160.9)
