#Ever since you started work at the grocer, you have been faithfully logging down each item and its category that passes through. One day, your boss walks in and asks, "Why are we just randomly placing the items everywhere? It's too difficult to find anything in this place!" Now's your chance to improve the system, impress your boss, and get that raise!
# 
# The input is a comma-separated list with category as the prefix in the form "fruit_banana". Your task is to group each item into the 4 categories Fruit, Meat, Other, Vegetable and output a string with a category on each line followed by a sorted comma-separated list of items.
# 
# For example, given:
# 
# "fruit_banana,vegetable_carrot,fruit_apple,canned_sardines,drink_juice,fruit_orange"
# 
# output:
# 
# "fruit:apple,banana,orange\nmeat:\nother:juice,sardines\nvegetable:carrot"

def group_groceries(groceries):
    categories = {"fruit": [], "meat": [], "other": [], "vegetable": []}
    for entry in groceries.split(","):
        category, item = entry.split("_")
        categories[category if category in categories else "other"].append(item)
    return "\n".join([f"{category}:{','.join(sorted(items))}" for category, items in categories.items()])
    
def group_groceries(groceries):
    from re import findall
    d = {key:[] for key in ('fruit', 'meat', 'other', 'vegetable')}
    for key, value in tuple((cat if cat in ('fruit', 'meat', 'vegetable') else 'other', name) for cat, name in findall(r'(\w+)_(\w+)', groceries)):
        d[key].append(value)
    return '\n'.join( key + ':'+','.join(sorted(d[key])) for key in sorted(d.keys()) )
