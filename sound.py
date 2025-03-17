from abc import ABC, abstractmethod
# Define an abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass # This is an abstract method, no implementation here.


# Concrete subclass of Animal
class dog(Animal):
    def sound(self):
        return "bark" # Providing the implementaltion of the abstract method
#Create an instamce of Dog
dog = dog ()
print(dog.sound()) # Output: Bark