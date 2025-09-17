# September 17, 2025


## Case 3 of Master Theorem
`T(n) = 2T(n/2) + n^2`, `a = 2`, `b = 2`, `f(n) = n^2`.

Using case 1, we need to find an `e` to make `n^2 = O(n^1-e)`. Which is not possible.

Using case 2, we need to find some `k` such that `f(n) = Theta(n^log_b(a) * log(n)^k)`. In this case we have `n^2 = Theta(n*log(n)^k)`. In which there is no `k` to make this true.

Using case 3, we need to find an `e` such that `f(n) = Omega(n^(log_b(a) + e))`. In our case `n^2 = Omega(n^log_2(2) + e)`. Which can simplify to `n^2 = Omega(n^1 + e)` where if we pick `e = 1/2` we get `n^2 = Omega(n^1.5)`. So yes there is a `e`.

For case 3, `T(n) = Theta(f(n)) = Theta(n^2)`. You will need to check the regularity condition.

You dont have to worry about it but if you want to its `af(n/b) <= cf(n)` for some `c`.

