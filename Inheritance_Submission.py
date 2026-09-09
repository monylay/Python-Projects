
class Animal:
    #attributes that all animals can have
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    #Dog class has two of its own attributes
    #breed and favorite_snack

    def __init__(self, name, age, breed, favorite_snack):

        #call the parent class to set name and age
        super().__init__(name, age)

        #these are attributes specific to Dog
        self.breed = breed
        self.favorite_snack = favorite_snack

class Cat(Animal):
    #the cat class has two of its own attributes
    #color and favorite_food

    def __init__(self, name, age, color, favorite_food):

        super().__init__(name, age)

        #these are attributes specific to Cat
        self.color = color
        self.favorite_food = favorite_food

#create Dog object

my_dog = Dog("Bear", 4, "Husky", "Beef")

#Create Cat Object
my_cat = Cat("Pomi", 7, "Calico", "Chicken & Beef")

#print dog info
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
print(my_dog.favorite_snack)

#print cat info
print(my_cat.name)
print(my_cat.age)
print(my_cat.color)
print(my_cat.favorite_food)
