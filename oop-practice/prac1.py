class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and I am a {self.breed}.")

# def main():
    dog1 = Dog("Buddy", 5, "Golden Retriever")
    dog1.speak()
    dog1.eat()