from vehicle import Vehicle
from honda import Honda
from suzuki import Suzuki , EMehran
from counter import Counter


print('without object')
print( Counter.total_counters )
Counter.counter_inc()
Counter.counter_inc()
Counter.counter_inc()
Counter.counter_inc()
Counter.counter_inc()
# Counter.display_count()
print( Counter.total_counters )



# make object
# v1 = Vehicle('Honda','Accord','Black','Auto')
v2 = Vehicle('Honda','Accord','Black','Auto')
# del v1

v2.display_all()
# v2.display_transmission

# v1.display_all()
# v1.display_brand()



# h1 = Honda('City','Red','Manual')
# h1.display_transmission()
# h1.display_brand()
# h1.honda_info()



# s1 = Suzuki('Mehran','Grey','Auto')
# s1.display_all()


# em1 = EMehran('Transparent')
# em1.display_all()
# em1.suzuki_history()
# em1.up_coming()


