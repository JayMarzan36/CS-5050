# August 27, 2025




## Example: Exponentiation (Algorithms section 1.10)

```
Slow_Power(a,n):
    x <- a
    for i <- 2 to n
        x <- x * a
    return x
```

The computation complexity is `O(n)`.

Any faster way?

```
for i <- 2 to n
    x **<- a
```

In class example of a better algorithm. Uses recursion, and times itself with the return of the recursive call.

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

The complexity of the `Pingala_Power` is `O(log(n))`.

## Example: Text Segmentation (Algorithms section 3.3)

Given a string of characters, can you segment it into words? (assume you have a constant time dictionary lookup).

HEARTHANDSATURNSPIN -> HEARTH AND SATURN SPIN


Using recursive backtracking
```
Splittable(A[1..n]):
    if n = 0
        return true
    for i <- 1 to n
        if is_word(A[1..i])
            if Splittable(A[i+1..n])
                return true
    return false
```

My guess to the complexity is `O(n^2)`.

The real complexity is `O(2^n)`. Its exponential.

*   The recursive call is inside the for loop. And when the recursive call is being called there is a for loop inside of each of the recursive calls. So its exponentially getting bigger.


The better version

**Note: the algorithm is not complete**
```
Fast_Splittable(A[1..n]):
    Splittable[n+1] <- true

    for i <-n down to 1
        splittable[i] <- false
        for j <- i to n
            if is_word(i,j)
```
