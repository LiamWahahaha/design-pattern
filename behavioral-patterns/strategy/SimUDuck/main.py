from abc import ABCMeta, abstractmethod

class FlyBehaviorInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fly') and
                callable(subclass.fly) or
                NotImplemented)

@FlyBehaviorInterface.register
class FlyWithWings:
    def fly(self):
        print(f"I'm flying!!")

@FlyBehaviorInterface.register
class FlyNoWay:
    def fly(self):
        print(f'Oops, I cannot fly...')

@FlyBehaviorInterface.register
class FlyRocketPowered:
    def fly(self):
        print(f"I'm flying with a rocket!")


class QuackBehaviorInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'quack') and
                callable(subclass.quack) or
                NotImplemented)

    @abstractmethod
    def quack(self):
        raise NotImplementedError

class Quack(QuackBehaviorInterface):
    def quack(self):
        print(f'Quack! Quack! Quack!')

class Squeak(QuackBehaviorInterface):
    def quack(self):
        print(f'Squeak! Squeak! Squeak!')


class MuteQuack(QuackBehaviorInterface):
    def quack(self):
        print(f'...(radio silience)')


class Duck:
    def __init__(self, fly, quack):
        self.__fly = fly
        self.__quack = quack

    def performQuack(self):
        return self.__quack.quack()

    def performFly(self):
        return self.__fly.fly()

    def swim(self):
        print(f'All ducks float, even decoys!')

    @abstractmethod
    def display(self):
        pass

    def setFlyBehavior(self, fly: FlyBehaviorInterface):
        self.__fly = fly

    def setQuackBehavior(self, quack: QuackBehaviorInterface):
        self.__quack = quack

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), MuteQuack())

    def display(self):
        print("I'm a model duck")

if __name__ == '__main__':
    mallard_duck = MallardDuck()
    mallard_duck.display()
    mallard_duck.performQuack()
    mallard_duck.performFly()
    model_duck = ModelDuck()
    model_duck.display()
    model_duck.performFly()
    model_duck.setFlyBehavior(FlyRocketPowered())
    model_duck.performFly()