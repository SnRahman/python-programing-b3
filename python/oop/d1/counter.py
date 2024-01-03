class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display_count(self):
        print(f'current count is : {self.count}')

c1 = Counter()
c1.display_count()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.display_count()


c2 = Counter()
c1.display_count()
c2.increment()
c2.increment()
c2.increment()
c2.increment()
c2.display_count()