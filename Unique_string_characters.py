
# you will be given two strings a and b and your task will be to return 
# the characters that are not common in the two strings. 


def solve(a,b):
    return "".join([c for c in a if not c in b]+[c for c in b if not c in a])

def solve(a,b):
    s = set(a)&set(b)
    return ''.join(c for c in a+b if c not in s)
    
 solve=lambda a,b:a.translate(str.maketrans("","",b))+b.translate(str.maketrans("","",a))
