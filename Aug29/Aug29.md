# August 29, 2025
Review of `Big O`.

Try to ignore hardware when analyzing `Big O`. But hardware can play a role.

## Formal `Big O` definition

`Big O` upper bound.

``` python
O(g(n)) = {f(n)|Ec,n_0 > 0 s.t. 0 <= f(n) <= cg(n), An >= n_0}
```

There exist some positive constants such that g(n) is within a constant of f(n) for large inputs.

## Formal `Big Omega` definition

`Big Omega` lower bound.

```python
Omega(g(n)) = {f(n)|Ec,n_0 > 0 s.t. 0 <= cg(n) <= f(n), An >= n_0}
```

## Formal `Big theta` definition

`Big Theta` is both lower and upper bound.

```python
Theta(g(n)) = {f(n)|Ec_1, c_2, n_0 > 0 s.t. 0 <= c_1g(n) <= f(n) <= c_2g(n), An >= n_0}
```


`Big O` is used more often because its good enough.


Take the limit of f(n)/g(n). If the limit is 0 => O(f(n)), Positive real number => Theta(f(n)), Infinity => Omega(f(n)).