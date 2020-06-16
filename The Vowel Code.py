# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
# 
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# 
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
# 
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
# 
# For example, decode("h3 th2r2") would return "hi there".
# 
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.



code = {"a":'1', "e":'2', "i":'3', "o":'4', "u":'5'}

def encode(st):
    return ''.join(str(code[char]) if char in code.keys() else char for char in st)

def decode(st):
    return ''.join(list(code.keys())[list(code.values()).index(char)] if char in code.values() else char for char in st)
    
# Cleverer    
    
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
    
    
 
