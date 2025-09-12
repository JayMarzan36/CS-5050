# September 12, 2025
Week 3 discussion

## Consider **stooge** sort, an inefficient but correct recursive algorithm for sorting an array

```
function stoogesort(A[], lo, hi) {
    if (A[lo] > A[hi])
        swap(A[lo], A[hi])
    if (hi - lo + 1 >= 3) {
        oneThird = floor((hi -lo + 1) / 3);
        stoogesort(A, lo, hi - oneThird)
        stoogesort(A, lo + oneThird, hi)
        stoogesort(A, lo, hi - oneThird)
    }

    return A
}
```

Find runtime complexity

Would the `T(n)` function be, `T(n) = 3T(n2/3)  + c`




```
function stoogesort(A[], lo, hi) {
    if (A[lo] > A[hi])---comparison
        swap(A[lo], A[hi])----constant
    if (hi - lo + 1 >= 3) {---comparison
        oneThird = floor((hi -lo + 1) / 3);---dividing the problem by 2/3
        stoogesort(A, lo, hi - oneThird)-------
        stoogesort(A, lo + oneThird, hi)      | 3 recursive calls
        stoogesort(A, lo, hi - oneThird)-------
    }

    return A
}
```