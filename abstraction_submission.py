
from abc import ABC, abstractmethod

#Parent class
#abc means this class is an abstract base class
class Animal(ABC):

    #abstract method, the parents say that every child class must have this method
    @abstractmethod
    def makeSound(self):
        pass

    #regular method, child classes automtically inherit this method
    def wake(self):
        print("The cat is awake.")


#child class
class Cat(Animal):

    #child class provides the actual implementation of the parents abstract method
    def makeSound(self):
        print("The cat says: Meow!")

#create an object from the child class
myCat = Cat()

#use abstract method that the cat class implemented
myCat.makeSound()

#use regular method inherited from the Animal class
myCat.wake()
