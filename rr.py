
__author__ = "Jura Šolja"
__email__ = "jursolja@foi.hr"

from math import sqrt
import argparse

class Tocka:
    """
        Opis ove klase.
        2-dim tocke u ravnini.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
            
    def __repr__(self):
        return "Tocka({0}, {1})".format(self.x,self.y)
    
class Vektor(Tocka):
    
    def __add__(self, b):
        """
        Self je vektor, b je vektor.
        """
        x = self.x + b.x
        y = self.y + b.y
        return Vektor(x, y)
    
    def __sub__(self, b):
        x = self.x - b.x
        y = self.y - b.y
        return Vektor(x, y)
    
    def __mul__(self, b):
        if(type(b) == type(self)):
            return self.x * b.x + self.y * b.y
        else:
            return Vektor(self.x * b, self.y * b)
    
    __rmul__ = __mul__
        
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return "Vektor({0}, {1})".format(self.x,self.y)