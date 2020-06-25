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
   
