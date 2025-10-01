# September 15, 2025

4 Methods to solving recurrences ([[Solving Recurrences by Unrolling]])
*   Expanding the recurrence
*   Recursion trees
*   Guess-and-verify
*   Master Theorem/Master Method

Used for any recurrence of this form `T(n) = aT(n/b) + f(n)` **has to be**. Where `a >= 1, b > 1` and `f(n)` is an asymptotically nonnegative function defined over all sufficiently large positive numbers. (the function doesnt return a negative)

`f(n)` is the deriving function.

If you have ceil or/and floor, throw them out and just combine them.

There are 3 cases that have to be taken into consideration aswell.


### Example of using Master theorem
Using the recurrence from the in class discussion from `Sep12`.
```
T(n) = 3T(2/3 * n) + 1

a = 3

b = 3/2

f(n) = 1
```

#### Case 1
We need to find some `e` greater than `0` such that `f(n) = O(n^log_b(a-e))`.

Plugging in, we need `e` such that `1 = O(n^log_3/2(3-e))`

Yes, it exists (all you really need to show is that some `e` exists)

Therefore `T(n) = Theta(n^log_b(a)) = Theta(n^log_3/2(3))`



### Example with merge sort
```
T(n) = 2T(n/2) + n

a = 2

b = 2

f(n) = n
```

#### Case 1
We need to find some `e` greater than `0` such that `f(n) = O(n^log_b(a))`.

In this case `n = O(n^log_2(2-e)) = O(n^1 - e)`, in this case it fails.

It fails because there is no `e` where `n` could be equal to `O(n^1 - e)`.


#### Case 2
We need to find some `k` greater than equal to `0` such that `f(n) = Theta(n^log_b(a) * lg^k(n))`. (`lg^k(n)` is `log(n)^k`)

In our case `n = Theta(n^log_b(a) * lg^k * n)`. Picking `k` to be 0, we get `n = Theta(n * lg^0*n) = Theta(n)`.

Yes.