from observer_ex1 import Publisher, Subscriber

publisher = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

publisher.register(bob)
publisher.register(alice)
publisher.register(john)

publisher.dispatch("It's lunchtime!")

publisher.unregister(john)

publisher.dispatch("Time for dinner!")