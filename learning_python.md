# Learning Python  
print()  
input()

## Control Flow Tools
### `if` Statements
```
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.


### `for` Statements  
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


### `range()` Function
It generates arithmetic progressions:

```
>>> for i in range(5):
...     print(i)
...
0
1
2
```

The given end point is never part of the generated sequence. It is possible to let the range start at another number, or to specify a different increment (‘step’)
`range(start_point, end_point, step)`

```
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]
```

To iterate over the indices of a sequence, you can combine range() and len()

```
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

The object returned by range() it's an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

```
>>> range(10)
range(0, 10)

>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

### `break` Statements 
The `break` statement breaks out of the innermost enclosing for or while loop.

### `else` Clause
A for or while loop can include an else clause.   
In a for loop, the else clause is executed after the loop reaches its final iteration.  
In a while loop, it’s executed after the loop’s condition becomes false.  
In either kind of loop, the else clause is not executed if the loop was terminated by a break.

```
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     # else clause belongs to the for loop
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

### `continue` Statements
It's used to skip the rest of the code inside a loop for the current iteration, and it continues with the next iteration of the loop.

```
>>> for num in range(2, 6):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
```

### `pass` Statements
The pass statement does nothing.  
It can be used when a statement is required syntactically but the program requires no action.
It can be used is as a place-holder for a function or conditional body when you are working on new code.


### `match` Statements
A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.  

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
 
You can combine several literals in a single pattern using | (“or”):

```
case 401 | 403 | 404:
    return "Not allowed"
```

## Function  


## Semantic Versioning (SemVer)
In SemVer, version numbers are given in the format of 
```
MAJOR.MINOR.PATCH
```
* MAJOR version changes when you make incompatible API changes
* MINOR version changes when you add functionality in a backwards compatible manner, and
* PATCH version changes when you make backwards compatible bug fixes.

