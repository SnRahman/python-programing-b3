from vehicle import Vehicle

class Honda(Vehicle):

    def __init__(self,model,color,transmission):
       super().__init__('Honda',model,color,transmission)
    #    Vehicle.__init__('Honda',model,color,transmission)
    
    def honda_info(self):
        print('Honda has been the world \'s largest motorcycle manufacturer since 1959,[3][4] reaching a production of 400 million by the end of 2019')

 
# h1 = Honda('City','Red','Manual')
# h1.display_transmission()
# h1.display_brand()
# h1.honda_info()