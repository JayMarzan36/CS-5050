# September 24, 2025
([[Divide and Conquer Intro]])
## 1st Algorithm
Suppose you are given an array `A` with `n` entries, with each entry holding a distinct number. You are told that the sequence of values `A[1], A[2], . . . , A[n]` is unimodal: For some index `p` between `1` and `n`, the values in the array entries increase up to position `p` in `A` and then decrease the remainder of the way until position `n`. (So if you were to draw a plot with the array position `j` on the x-axis and the value of the entry `A[j]` on the y-axis, the plotted points would rise until x-value `p`, where they’d achieve their maximum, and then fall from there on.)

You’d like to find the “peak entry” `p` without having to read the entire array-in fact, by reading as few entries of `A` as possible. Show how to find the entry `p` by reading at most O(log n) entries of `A`.



```python
function peak_entry(array, left=0, right=None):
 
    if right is None:
 
        right <- len(array) minus 1
 
    mid <- (left add right) divide 2
 
    if (mid equal to 0 or array[mid] greater than or equal to array[mid minus 1]) and (mid equal to len(array) minus 1 or array[mid] greater than or equal to array[mid add 1]):

        return mid
 
    if mid greater than 0 and array[mid minus 1] greater than array[mid]:
 
        return peak_entry(array, left, mid minus 1)
 
    else:
 
        return peak_entry(array, mid add 1, right)
```


## 2nd Algorithm
Your are given `k` sorted lists `L1, L2, . . . , Lk`, with `1 ≤ k ≤ n`, such that the total number of the elements in all `k` lists is `n`. Note that different lists may have different numbers of elements. We assume that the elements in each sorted list `Li`, for any `1 ≤ i ≤ k`, are already sorted in ascending order.

Design a divide-and-conquer algorithm to sort all these n numbers. Your algorithm should run in `O(n log k)` time (instead of `O(n log n)` time).

Note: An `O(n log k)` time algorithm would be better than an `O(n log n)` time one when `k` is sufficiently smaller than `n`. For example, if `k = O(log n)`, then `n log k = O(n log log n)`, which is strictly smaller than `n log n` (i.e., `n log log n = o(n log n)`).

The following gives an example. There are five sorted lists (i.e., `k = 5`). Your algorithm needs to sort the numbers in all these lists.

`L1 : 3, 12, 19, 25, 36`
`L2 : 34, 89`
`L3 : 17, 26, 87`
`L4 : 28`
`L5 : 2, 10, 21, 29, 55, 59, 61`