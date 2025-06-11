# Create a list
fruits = ['apple', 'banana', 'cherry']

# Add elements
fruits.append('orange')       # ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'kiwi')      # Insert at index 1

# Remove elements
fruits.remove('banana')       # Removes first occurrence
popped = fruits.pop()         # Removes and returns last item
del fruits[0]                 # Deletes element at index 0

# Access and modify
print(fruits[1])              # Access
fruits[1] = 'mango'           # Modify

# Slicing
print(fruits[1:3])            # ['mango', 'cherry']




squares = [x**2 for x in range(10)]   # [0, 1, 4, ..., 81]
evens = [x for x in range(10) if x % 2 == 0]


# Create a dictionary
person = {'name': 'Alice', 'age': 25}

# Access
print(person['name'])        # Alice
print(person.get('age'))     # 25

# Add or update
person['city'] = 'New York'
person['age'] = 26

# Remove
del person['age']
city = person.pop('city')    # Returns the value

# Keys, values, items
print(person.keys())         # dict_keys(['name'])
print(person.values())       # dict_values(['Alice'])
print(person.items())        # dict_items([('name', 'Alice')])


squares = {x: x**2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, ...}
