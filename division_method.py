def hash_division(key, size):
    # Returns the hash table index for the given key by division
    return key % size

hash_table = [] # create a hash table with 10 elements
keys = [3, 7, 12, 15, 21, 27, 31, 42, 56, 63] # list of keys
for key in keys:
    index = hash_division(key, len(keys)) # calculate the index for the key
    hash_table.append(index) # store the key in a hash table
print(hash_table) 



