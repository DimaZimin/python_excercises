#Largest palindrome made of two 3x digits product 

def palindrome():
    n = 0
    for a in range(999, 100, -1):
        for b in range(a, 100, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b
                    break
                else:
                    continue
    return n
   
###################################################################################################################################################
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 21):
     n = lcm(n, i)

###################################################################################################################################################
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.   
def sumofsq():
    return sum([x*x for x in range(1, 101)])

def squareofthesum():
    return sum([x for x in range(1, 101)])**2
print(squareofthesum() - sumofsq())
#25164150

###################################################################################################################################################
#Find N adjacent digits in the Y number that have the greatest product. What is the value of this product?
# Y - iterable (big_num), X - N chunk size(adj_digits)

from functools import reduce
import operator

#This functions cuts a big number into evenly sized chunks of adjacent digits
def cut_adj_chunks(iterable, chunk_size):
    for i in range(len(iterable) - chunk_size):
        yield iterable[i:i + chunk_size]
# This sums the product of the chunks
def sum_prod(num_str):
    num_list = map(int, num_str)
    return reduce(operator.mul, num_list, 1)
#A main function that returns the largest adjecent product
def largest_prod(adj_digits, big_num):
    return max(sum_prod(chunk) for chunk in cut_adj_chunks(str(big_num),adj_digits))

###################################################################################################################################################
#Print N prime numbers:
#This checks if number is prime
def is_prime(number):
    if number >= 2:
        for i in range(2, number):
            if not (number % i):
                return False
    else:
        return False
    return True
#this returns the N'th prime number (NOT OPTIMISED SOLUTION)
def n_prime(quantity):
    primes = []
    n = 2
    while len(primes) != quantity:
        for i in range(n, n + 1):
            if is_prime(i):
                primes.append(i)
                n += 1
                print(primes)
            else:
                n += 1
    return primes[-1]
###################################################################################################################################################
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def check_if_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


def loop():
    for a in range(1, 1000):
        for b in range(a, 1000):
            if check_if_triplet(a, b, (1000 - (a + b))):
                return a * b * (1000 - (a + b))


