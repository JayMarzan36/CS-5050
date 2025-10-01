# September 8, 2025

## Problem - Getting Ready for Merge Sort

How would you combine two sorted lists so that the result is a sorted list conatining the elemnts of both lists?

I would iterate through both inputs and check to see if one is less than or equal to the other and depending on the result I would append that to an array that will hold the final array.

Mergesort full pseudo-code



Recursive
```python
Merge_Sort(A[1...n])
    if n > 1
        m <- floor(n/2)

        Merge_Sort(A[1 ... m])
        Merge_Sort(A[m+1 ... n])
        Merge(A[1...n], m)
```


Iterative
```python
Merge(A[1 ... n] , m)
    i <-; j <- m + 1

    for k <- 1 to n
        if f > n
            B[k] <- A[i]; i <- i + 1
        else if i > m
            B[k] <- A[j]; j <- j + 1
        else if A[i] < A[j]
            B[k] <- A[i]; i <- i + 1
        else

        rest of the code is in the slides
```



```python
T(n) = T(floor(n/2)) + T(ceil(n/2)) + Theta(n)

     = 2T(n/2) + Theta(n)
```



Recurrence by Recursion tree
Only focus on the work being done by the current call
```

                                  O(n)       Work done = O(n)
                                  / \
                             O(n/2) O(n/2)   Work done = O(n/2) + O(n/2) = O(n)
                                /     \
                            O(n/4)   O(n/4)  Work done = O(n/4) + O(n/4) = O(n)
                              /         \
                              .          .
                              .          .
                            O(1)       O(1)

```
Size of tree is `log(n)`




```
level 0 = 1 node, work n at each node
level 1 = 2 node, work n/2 at each node
level 2 = 4 node, work n/4 at each node
level k = 2^k nodes, work n/2^k at each node


n/2^k = 1

n = 2^k

log(n) = log_2(2^k)

log_2(n) = k

log_2(n) levels, n work at each level

O(nlog(n))
```
