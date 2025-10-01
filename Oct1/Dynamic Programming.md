# Oct 1

## bottom-up dynamic programming
Figure out what values you are going to need, fill them in from the start.

* Code is often shorter and more readable
* The code can be more difficult to design initially, but is easier to debug

## top-down
Break problem into smaller chunks and solve.

## Pattern/Steps
1. Formulate the problem recursively
	* a) Identify subproblems
	* b) Choose a memoization data structure
	* c) Identify dependencies
	* d) Find a good evaluation order
		* Which order to solve subproblems in
	* e) Analyze space and running time
		* How many things are your filling in and how long does it take to fill in
	* f) Write down the algorithm
2. Build solutions to your recurrence from the bottom up

### Example
#### Calculate the nth fibonacci number
1. Recursively, `fib(n) = fib(n-1) + fib(n-2)`
	1. a) Solve `fib(k)` for any `k < n`
	2. b) Use a 1d array
	3. c) Find base case, `fib(0)` and `fib(1)`
	4. d) Start with the smallest and work your way up
	5. e) Runtime: n things to solve at constant time. So `O(n)`
	6. f) Write down the algorithm
2. Build the solution!

```python
def fib(n):
	store = []
	store[0] = 0
	store[1] = 1
	for i in range(2, n + 1):
		store[i] = store[i - 1] + store[i - 2]
	return store[n]
```

#### Splittable
Given a string of Characters can we split it into words?
1. Recursively, `splittable(A[i,..,n]) = { true if i > n; V_(j=1) ^n (is_word(A[i,..,j] and splittable(A[j + 1,...,n]))`
	1. a) Is `A[i + 1,..,n]` a word, up to the empty string. 
	2. b) Use a 
	3. c) Dependencies are is `is_word(A[i,...,j])`