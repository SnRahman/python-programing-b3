class Car:

    # declare hard values
    # def __init__(self):
    #     self.brand = 'Honda'
    #     self.model = 'Civic'
    #     self.color = 'White'
    #     self.transmission = 'Auto'
    

    def __init__(self,brand,model,color,transmission):
        self.brand = brand
        self.model = model
        self.color = color
        self.transmission = transmission

    def display_brand(self):
        print(f'Brand is : {self.brand}')
    
    def display_model(self):
        print(f'Model is : {self.model}')

    def display_color(self):
        print(f'Color is : {self.color}')

    def display_transmission(self):
        print(f'Transmission is : {self.transmission}')

    def display_all(self):
        print(f'Brand is : {self.brand}')
        print(f'Model is : {self.model}')
        print(f'Color is : {self.color}')
        print(f'Transmission is : {self.transmission}')



c1 = Car('Toyota','Corolla','White','Manual')
# print( type(c1))
c1.display_all()

c2 = Car('Honda','City','Red','Manuall')
# c2.display_all()
c2.display_brand()
c2.display_model()

