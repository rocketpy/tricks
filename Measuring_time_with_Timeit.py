#  Measure execution time of small code snippets 

#  Docs: https://docs.python.org/3/library/timeit.html

#  Good example

#  Generating integers 
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
    return results


import timeit

start_time = timeit.default_timer()
gen_prime(1000)
print(timeit.default_timer() - start_time)


# or
"""
import timeit


print(timeit.timeit(

limit = 1000
prime_list = [i for i in range(2, limit+1)]

for prime in prime_list:
    for elem in range(prime*2, max(prime_list)+1, prime):
        if elem in prime_list:
            prime_list.remove(elem)

, number=10))

"""

# in CMD
# python -m timeit -c "$(cat file_name.py)"

# from the docs
"""
The following example shows how the Command-Line Interface can be used to compare three different expressions:

$ python3 -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 5: 30.2 usec per loop
$ python3 -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 5: 27.5 usec per loop
$ python3 -m timeit '"-".join(map(str, range(100)))'
10000 loops, best of 5: 23.2 usec per loop

This can be achieved from the Python Interface with:
>>>

>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
0.3018611848820001
>>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
0.2727368790656328
>>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
0.23702679807320237
"""

