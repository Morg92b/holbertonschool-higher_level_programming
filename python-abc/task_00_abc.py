#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class that defines the blueprint for animals
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses,
        representing the sound the animal makes
        """
        pass


class Dog(Animal):
    """
    A subclass of Animal that represents a dog
    """
    def sound(self):
        """
        Returns the sound made by a dog
        """
        return "Bark"


class Cat(Animal):
    """
    A subclass of Animal that represents a cat
    """
    def sound(self):
        """
        Returns the sound made by a cat
        """
        return "Meow"
