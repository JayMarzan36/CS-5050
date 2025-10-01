# September 19, 2025

Week 4 Discussion
([[Master Theorem and Master Method]])

## Show that determining if a number is in a balanced binary search tree with n elements is O(log(n))
The depth of a balanced binary search tree is `O(log(n))`. When searching for a number you only go down one side at a time so there is only one recursive call per layer.

The recurrence is `T(n) = T(n/2) + Theta(log(n))`. Using case 1 of the master theorem you will end with `T(n) = Theta(log(n))`.

## Solve the following recurrences using the master theorem, or state if the master theorem cannot be used to solve the recurrence

### T(n) = 27T(n/3) + Theta(n^3 * log(n))
Use case 2 of the master theorem.

Final `T(n) = Theta(n^3 * log(n))`.

### T(n) = 27T(n/3) + Theta(n^3 / log(n))
Can't use the master theorem.

### T(n) = 5T(n/2) + Theta(n^3)
Use case 3 of the master theorem.

Final `T(n) = Theta(n^3)`.

### T(n) = 5T(n/2) + Theta(n^2)
Use case 1 of the master theorem.

Final `T(n) = Theta(n^2.321)`.