# September 3, 2025
Notes on tim ecomplexity.
1.  Constants don't matter
2.  Polynomial order matters: n^b in O(n^a) for a >= b
3.  Exponential dominates polynomial
4.  Exponential base matters
5.  Polynomial dominates logarithm
6.  Logarithm base doesn't matter



*   O(n1)            Worst
*   O(c^n)             |
*   O(n^c)             |
*   O(nlog(n))         |
*   O(n)               |
*   O(log(n))        Best

## Solving Recurrences by unrolling

Function
```python
def factorial(x):
    if x <= 1:
        return 1
    return factorial(x-1) * x
```


My guess
```python
T(x) = 3 + T(x-1)
```

Actuall
```python
T(x) = 4 + T(x-1)
```

The 4 comes from: 1 comparison, 1 function call, 1 subtraction, 1 multiplication.


### Unrolling the function (Solving recurrences)

```python
T(x) = T(n-1) + 4, T(1) = 2
```

Whats `T(n-1)`?

`T(n-1) = T((n-1) - 1) + 4` plug back into the function.

`T(n) = T(n-2) + 4 + 4` Unrolled once. Lets do it again.

`T(n) = T(n-3) + 4 + 4 + 4` Unrolled twice. Another.

`T(n) = T(n-4) + 4 + 4 + 4 + 4`. What if we unrolled `k` times?

`T(n) = T(n-k) + 4k`. How many unrolls (value of `k`) until we hit the base case?

Base case is `T(1) = 2`.

When `n-k = 1` we will have hit the base case. Now solve for `k`, `k = n - 1`. From this we see that we will need to unroll `n - 1` times to hit the base case.

`T(n) = T(n-k) +4k`

`T(n) = T(n - (n - 1)) + 4n - 4`

`T(n) = T(1) + 4n - 4`

`T(n) = 2 + 4n - 4`

`T(n) = 4n - 2`

Time complexity is `O(n)`.



## Pingala Power Recurrence

```
Pingala_Power(a,n):
    if n = 1
        return a
    else
        x <- Pingala_Power(a, floor(n/2))
        if n is even
            return x * x
        else
            return x * x * a
```

Note: You can ignore floor and ceiling functions.

Base case is `Pingala_Power(a,1)`, `T(1) = 2`.

Our `T(x)` function is, `T(n) = T(n/2) + 9`.

### Unrolling
`T(n/2) = T((n/2)/2) + 9`

`T(n) = T(n/4) + 9 + 9`

`T(n) = T(n/8) + 9 + 9 + 9`

`T(n) = T(n/2^k) + 9k`

At what `k` do we hit the base case?

`n/2^k = 1`

`n = 2^k`

`log(n) = log(2^k)`

`log(n) = k log(2)`

`k = log(n)/log(2)`

`k = log_2(n)`

Plug this in for `k`.

`T(n) = T(n/2^(log_2(n))) + 9log_2(n)`

`T(n) = T(n/n) + 9log_2(n)`

`T(n) = T(1) + 9log_2(n)`

`T(n) = 2 + 9log_2(n)`

Time complexity is `O(log(n))`.