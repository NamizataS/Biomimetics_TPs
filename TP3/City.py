"""
Class City that will allow us to create and handle our cities.
These are simply our (x,y) coordinates. We had the distance calculation making use of the Pythagorean theorem.
"""
import numpy as np


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # calculer la distance entre deux villes grâce au théorème de Pythagore
    def distance(self, city):
        x_dis = abs(self.x - city.x)
        y_dis = abs(self.y - city.y)
        distance = np.sqrt((x_dis ** 2) + (y_dis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
