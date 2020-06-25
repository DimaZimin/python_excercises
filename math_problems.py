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
   

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 21):
     n = lcm(n, i)
        
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.   
def sumofsq():
    return sum([x*x for x in range(1, 101)])

def squareofthesum():
    return sum([x for x in range(1, 101)])**2
print(squareofthesum() - sumofsq())
#25164150
