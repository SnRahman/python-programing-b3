class Counter:
    # static properties
    total_counters = 0


    def __init__(self):
        self.count = 0
        Counter.counter_inc()

    def increment(self):
        self.count += 1

    def display_count(self):
        print(f'current count is : {self.count}')

    @staticmethod
    def counter_inc():
        Counter.total_counters += 1



# print('counter 1')
# c0 = Counter()
# print( c0.total_counters )
# c0.counter_inc()
# print( c0.total_counters )

# print('counter 2')
# c1 = Counter()
# print( c1.total_counters )

# print('counter 3')
# c2 = Counter()
# print(c2.total_counters)


# print('without object')
# print( Counter.total_counters )
# Counter.counter_inc()
# Counter.counter_inc()
# Counter.counter_inc()
# Counter.counter_inc()
# Counter.counter_inc()
# Counter.display_count()
# print( Counter.total_counters )





c1 = Counter()
c1.display_count()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.display_count()
print( Counter.total_counters )


c2 = Counter()
c2.display_count()
c2.increment()
c2.increment()
c2.increment()
c2.increment()
c2.display_count()

print( Counter.total_counters )
