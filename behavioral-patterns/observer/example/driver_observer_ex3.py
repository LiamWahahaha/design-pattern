from observer_ex3 import Publisher, Subscriber

publisher = Publisher(['lunch', 'dinner'])
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

publisher.register("lunch", bob)
publisher.register("dinner", alice)
publisher.register("lunch", john)
publisher.register("dinner", john)

publisher.dispatch("lunch", "It's lunchtime!")
publisher.dispatch("dinner", "Dinner is served")