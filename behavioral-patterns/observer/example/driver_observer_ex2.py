from observer_ex2 import Publisher, SubscriberOne, SubscriberTwo

publisher = Publisher()
bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john = SubscriberTwo('John')

publisher.register(bob, bob.update)
publisher.register(alice, alice.receive)
publisher.register(john)

publisher.dispatch("It's lunchtime!")
publisher.unregister(john)
publisher.dispatch("Time for dinner")