#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Intent
# Provide an interface for creating families of related or dependent objects without specifying their concrete classes

# AbstractFactory


class MexicanRestaurants:
    def make_burrito(self):
        return

    def order_taco(self):
        return

# ConcreteFactory


class CovinaFoodTruck(MexicanRestaurants):
    def order_burrito(self):
        return

    def order_taco(self):
        return


class ElFarolito(MexicanRestaurants):
    def order_burrito(self):
        return

    def order_taco(self):
        return

# AbstractProduct


class FoodProduct:
    def prepare(self):
        return

    def wrap(self):
        return

    def box(self):
        return

# ConcreteProduct


class Burrito(FoodProduct):
    def prepare(self):
        return

    def wrap(self):
        return

    def box(self):
        return


class Taco(FoodProduct):
    def prepare(self):
        return

    def wrap(self):
        return

    def box(self):
        return



# Client


class Burritophile:
    def __init__(self,MexicanRestaurants = None):
        self.restaurant = MexicanRestaurants

    def order_food(self):





