# function for creating a data
import timeit
import random as rnd


def create_data():
    words = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
         'Hi', 'Hello', 'Welcome', 'World']
    data = rnd.choices(words, k=500000)
    return data


# using if/else
def test_if(data):
    for word in data:
        if word in ['World', 'Day', 'Happy', 'Hi']:
            pass
        elif isinstance(word, int):
            pass
        elif isinstance(word, str) and len(word) > 3:
            pass
        elif isinstance(word, str) and word.startswith("H"):
            pass
        else:
            pass
        

# using match/case
def test_match(data):
    for word in data:
        match word:
            case 'World'|'Day'|'Happy'|'Hi':
                pass
            case int(word):
                pass
            case str(word) if len(word) > 3:
                pass
            case str(word) if word.startswith("H"):
                pass
            case _:
                pass
            


test_data = create_data()

repeats = 100

time_repeat_if = timeit.timeit("test_if(test_data)",
                               setup="from __main__ import test_if, test_data",
                               number=repeats)

time_repeat_match = timeit.timeit("test_match(test_data)",
                                  setup="from __main__ import test_match, test_data",
                                  number=repeats)

print("Result: IF/ELSE: ", time_repeat_if/repeats)
print("Result MATCH/CASE: ", time_repeat_match/repeats)

