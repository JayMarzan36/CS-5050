# September 10
For homework the math format equations are using python for the interperation
([[Solving Recurrences by Unrolling]])
This is one that can show up on the homework

```
Equations
T(n) = 3T(n/3) + 2T(n/2) + O(n^2), T(1) = 1

T(n) = 3T(n/3) + 2T(n/2) + n^2


Recursion tree (not fully complete only showing some and not all)

                                                          T(n)      Level 0
                                                        / / | \ \
                                         T(n/3)  T(n/3)  T(n/3)  T(n/2)  T(n/2)     Level 1
                                           /                                \
                                          /                                  \
            T(n/9) T(n/9) T(n/9) T(n/2) T(n/2)             T(n/6)  T(n/6)  T(n/6)  T(n/4)  T(n/4) Level 2


Finding work at each level

T(n) = 3T(n/3) + 2T(n/2) + n^2


Work done at Level 0 = n^2

Work done at Level 1 = 3(3T(n/9) + 2T(n/6) + (n^2 / 3)) + 2(3T(n/6) + 2T(n/4) + (n^2 / 2)) + n^2
                     
                     = 9T(n/9) + 6T(n/6) + n^2/3 + 6T(n/6) + 4T(n/4) + n^2 / 2 + n^2
                     
                     = 9T(n/9) + 12T(n/6) + 4T(n/4) + n^2/3 + n^2/2 + n^2
                     
                     = 2n^2/6 + 3n^2/6
                     
                     = 5n^2/6


Work done at Level 2 = 
                     
                       Take 9T(n/9) => 9 (n/9)^2 = n^2/9
                       
                       Take 12T(n/6) => 12 (n/6)^2 =
                       
                       Take 4T(n/4) => 4 (n/4)^2 = n^2/4
                     
                     = 25/36 * n^2 


Work at levels; n^2, 5/6 * n^2, 25/36 * n^2, level i : (5/6)^i * n^2

Decreasing geometric sequence (calculus)
```

You find the work done by the recursion (look at how we found work at level 2) and add them up and that is the work.

The goal is to be able to just look at the recurrence functions `T(n) = somthing` and figure out what the complexity is.


## Divide and Conquer ([[Divide and Conquer Intro|Divide and Conquer Intro]])
*   **Divide**
    *   Divide the problem into a number of (usually 2) **subproblems** that are smaller instances of the original problem

*   **Conquer**
    *   Solve the **subproblems** recursively
    *   Base case: If the **subproblems** is small enough (constant size), solve it in a straight forward way

*   **Combine**
    *   Combine the solutions to the **subproblems** into a solution to the original problem



### Finding the largest number
Input: an array A[1,...,n] of n elements
Output: the largest number of A

A divide-and-conquer algorithm
*   **Divide**
    *   Divide A[1,...,n] into two subarrays A[1,...,n/2] and A[n/2 + 1,...,n] of roughly equal sizes

* **Conquer**
  * Find the largest number `max1` from A[1,...,n/2]
  * Find the largest number of `max2` from A[n/2 + 1,...,n]

* **Combine**
  * Returh the larger of the `max1` and `max2`


### Maximum-subarray
Input: an array A[1,...,n] of n numbers
Output: A **maximum subarray**