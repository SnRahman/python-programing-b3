class Person:

    def __init__(self,name,color,age,height,gender,blood_group):
        self.name = name
        self.color = color
        self.age = age
        self.height = height
        self.gender = gender
        self.blood_group = blood_group


    def display_all(self):
        print(f'Name : {self.name}')
        print(f'Color : {self.color}')
        print(f'Age : {self.age}')
        print(f'Height : {self.height}')
        print(f'Gender : {self.gender}')
        print(f'Blood Group : {self.blood_group}')


p1 = Person('Farhat','Gandami',45,5.2,'trans','O-')
p1.display_all()