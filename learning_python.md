# Learning Python  
print()  
input()

## Control Flow Tools  
#### `for` Statements  
Iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
```
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

cat 3
window 6
defenestrate 12
```

To modify a collection, it's better to loop over a copy of the collection or to create a new collection:

```
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Javier': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

#### `range()` Funtion