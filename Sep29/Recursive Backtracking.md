# September 29

### N-Queens Problem
Place `N-queens`  on an `NxN` chess board such that none of them can attack each other.

```python
PlaceQueens(Q[1,..,n], r):
  if r = n + 1 
    print Q[1,...,n]

  else 
    for j = 0 to n 
      legal = True 
      for i = 0 to r - 1
        if (Q[i] = j) or (Q[i] = j + r - i) or (Q[i] = j - r + i)
          legal = False
      
      if legal
        Q[r] = j
        placeQueens(Q[1,...,n], r + 1)
```

### Subset sum 
```python
SubsetSum(X, T)
  if T = 0
    return True
  else if T < 0 or X = []
    return False
  else
    x = any element of X 
    with = SubsetSum(X \ {x}, T - x)
    without = SubsetSum(X \ {x}, T)
    return (with or without)
```

The complexity is `O(2^n)`.

### All binary strings 

~~~python
def all_bin(prefix, n):
  if n == 0:
    print(prefix)
    return


  all_bin(prefix + "1", n - 1)
  all_bin(prefix + "0", n - 1)
  return

all_bin("", 6)
```
