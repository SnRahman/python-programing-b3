class Vehicle:

    def __init__(self,brand,model,color,transmission):
        self.brand = brand
        self.model = model
        self.color = color
        self.transmission = transmission
        print('object created')

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

    def __del__(self):
        print('object is deleted')
