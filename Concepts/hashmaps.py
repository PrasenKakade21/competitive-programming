# hash maps have a key:value pair 
# in Python dictionary is like a hashmap
# they find value in 0(1) time 
# one key can have multiple values
# keys must be immutable data type (you can’t change the object’s state after you’ve created it)
 
# initilize map
my_map = {}

# initilize key
my_map["prasen"] = []
print(my_map["prasen"])
my_map["manda"] = []

# Add values to key
my_map["prasen"].append(["kakade","bhimrao","hari"])
my_map["manda"].append(["kakade","bhimrao"])
print(my_map["prasen"])

#  use defaultdict as all the keys are already initialize
from collections import defaultdict
my_dict2 = defaultdict(int)
print(my_dict2["first"])
print(my_dict2["second"])

# retrivig data

# my_map.keys() gets list of keys
print(my_map.keys())
# my_map.values() gets list of values
print(my_map.values())
# my_map.items() gets list of key:value pair
print(my_map.items())