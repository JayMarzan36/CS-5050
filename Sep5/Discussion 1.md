# September 5, 2025
([[Solving Recurrences by Unrolling]])

1.  Let f and g be defined by f(n)=5^n, g(n) = 2^n. Which of the following are true?


    a.  f(n) in O(g(n))
    b.  f(n) in Theta(g(n))
    c. f(n) in Omega(g(n))


lim of f(n)/g(n) => 5^n / 2^n.


The limit is infinite so (c) is true, but since (c) is true the rest are also true (?).






2.  Let f and g be defined by f(n) = log_7(n), g(n) = log_4(n). Which of the following are true?

    a.  f(n) in O(g(n))
    b.  f(n) in Theta(g(n))
    c. f(n) in Omega(g(n))


With logorithms, we don't care about the base of the logorithm. So the growth of the two functions f and g are very close. And taking the limit of f(n)/g(n) we get `0.712414374216`. 

Since we got a positive real number, (b) is true.

1.  Let f and g be defined by f(n)=n^2.1, g(n) = n^2. Which of the following are true?


    a.  f(n) in O(g(n))
    b.  f(n) in Theta(g(n))
    c. f(n) in Omega(g(n))



Since `n` is in the base of both functions f and g. The limit f(n)/g(n) would reach infinity and not stop. (They would also grow pretty close together). But since the limit is infinity, (c) would be true, since (c) is true the rest are also true.

4.  Show that the recurrence  T(n) = T(n - 1) + n, T(1) = 1 is O(n^2).


`T(n) = T(n - 1) + n`

`T(n - 1) = T( (n-1) - 1) + T(n - 1)`

`T(n) = T(n - 2) + T(n - 1)`

`T(n) = T(n - 3) + T(n - 2)`

`T(n) = T(n - 4) + T(n - 3)`

`T(n) = T(n - k) + T(n - (k-1))`

`n - k = 1`

`n = 1 + k`

`n - 1 = k`

`T(n) = T(n - (n - 1)) + T(n - (n-2))`

`T(n) = T(1) + T(2)`

`T(n) = 1 + T(2)`

Time complexity is `O(n^2)`, we have an `n` from `T(1) = 1` and another `n` from `T(2)` (?).



5.  Show that the recurrence ([[Solving Recurrences by Unrolling]]) T(n) = T(n / 2) + Theta(1), T(1) = 1 is O(log(n)).

`T(n) = T(n / 2) + Theta(1)`

`T(n/2) = T(n / 4) + Theta(1) + Theta(1)`

`T(n) = T(n / 8) + Theta(1) + Theta(1) + Theta(1)`

`T(n) = T(n / 2^k) + Theta(1)k`

`n/2^k = 1`

`k = log_2(n)` This is from a previous notes (Sep3)

`T(n) = T(n/2^log_2(n)) + Theta(1)log_2(n)`

`T(n) = T(n/n) + Theta(1)log_2(n)`

`T(n) = T(1) + Theta(1)log_2(n)`

`T(n) = 1 + Theta(1)log_2(n)`

Time complexity is `O(log(n))`.


6.  Consider the following two algorithms for sorting an array A of n comparable values A[1], A[2], ... A[n].



Selection sort
```
for i = 1 -> n - 1 do
    jMin = i
    for j = i -> n do
        jMin = j
    swap A[i] and A[jMin]
```

Insertion sort
```
for i = 2 -> n do
    for j = i -> 2 do
        if A[j] < A[j-1] then
            swap A[j] and A[j-1]
        else
            break
```

a.  Find the best case and worst case runtimes of Selection Sort and Insertion Sort

Selection sort
Worst case: O(n^2), You are iterating through the array of n comparable values twice (2 for loops)
Best case: O(n^2), Even if you have a array of n = 1, you are still iterating through the n = 1 array twice (2 for loops)




Insertion sort
Worst case: O(n^2), Reason is same as Selection sort.
Best case: O(n^2), Same reason as Selection sort, even if your array is n = 1 you still are passing through the 2 for loops.



b.  True or False: In practice, insertion sort will always run at least as fast as selection sort

True, they have the same best and worst runtimes.


c.  True or False: The worst case runtime of Selection sort is Omega(n)

True,

d. True or False: The worst case runtime of Insertion sort is Omega(n^2)


7.  Show that the recurrence T(n) = 2T(n/2) + n is O(nlog(n))