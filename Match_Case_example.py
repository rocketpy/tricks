# function for creating a data
import random as rnd


def create_rnd_data():
    words = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
         'Hi', 'Hello', 'Welcome', 'World']
    data = rnd.choices(words, k=500000)
    return data
