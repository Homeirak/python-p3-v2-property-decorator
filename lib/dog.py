#!/usr/bin/env python3
#dog.py

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        
        self.name = name  #self.set_name(name)
        self.breed = breed #self.set_breed(breed)

    # def get_name(self):
    #     return self._name

    @property
    def name(self):
        """The name property"""
        return self._name
    
    # def set_name(self, name):
    #     if isinstance(name, str) and 1 <= len(name) <= 25:
    #         self._name = name.title()
    #     else:
    #         raise ValueError(
    #             "Name must be string between 1 and 25 characters.")

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    # name = property(get_name, set_name)

    # def get_breed(self):
    #     return self._breed

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    # def set_breed(self, breed):
    #     if breed in APPROVED_BREEDS:
    #         self._breed = breed
    #     else:
    #         raise ValueError("Breed must be in list of approved breeds.")

    @breed.setter
    def breed(self, breed):
        """Breed must be in the list of approved breeds"""
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    # breed = property(get_breed, set_breed)

# If we need methods for deleting the properties, we would decorate the methods with @name.deleter and @breed.deleter.

# The @property decorator must decorate the getter method, which should have the same name as the attribute.
# The docstring must go in the getter method.
# The setter and deleter methods must be decorated with the same name as the getter method plus .setter and .deleter, respectively.