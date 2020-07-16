from abc import ABCMeta, abstractmethod

class CashSuper(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'acceptCash') and
                callable(subclass.acceptCash) or
                NotImplemented)

    @abstractmethod
    def acceptCash(self, money):
        raise NotImplementedError

class CashNormal(CashSuper):
    def acceptCash(self, money):
        return float(money)

class CashRebate(CashSuper):
    def __init__(self, money_rebate):
        self.__money_rebate = money_rebate

    @property
    def money_rebate(self):
        return self.__money_rebate

    @money_rebate.setter
    def money_rebate(self, money_rebate):
        self.__money_rebate = money_rebate

    def acceptCash(self, money):
        return money * self.__money_rebate

class CashReturn(CashSuper):
    def __init__(self, money_condition, money_return):
        self.__money_condition = money_condition
        self.__money_return = money_return

    @property
    def money_condition(self):
        return self.__money_condition

    @property
    def money_return(self):
        return self.__money_return

    @money_condition.setter
    def money_condition(self, money_condition):
        self.__money_condition = money_condition

    @money_return.setter
    def money_return(self, money_return):
        self.__money_return = money_return

    def acceptCash(self, money):
        result = money
        return money - (money // self.__money_condition) * self.__money_return

class CashContext:
    def __init__(self, csuper):
        self.__cs = csuper

    @property
    def cs(self):
        return self.__cs

    @cs.setter
    def cs(self, csuper):
        self.__cs = csuper

    def getResult(self, money):
        return self.__cs.acceptCash(money)


if __name__ == "__main__":
    context = CashContext(CashNormal())
    print("Client: Strategy is set to Normal")
    print(context.getResult(100))
    print()

    print("Client: Strategy is set to Rebate (80%)")
    context.cs = CashRebate(0.8)
    print(context.getResult(100))
    print()

    print("Client: Strategy is set to Return")
    context.cs = CashReturn(40.0, 5.0)
    print(context.getResult(100))
    print()