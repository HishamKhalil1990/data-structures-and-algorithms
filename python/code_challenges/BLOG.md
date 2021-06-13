# Trace Selection Sort
### input [8,4,23,42,16,15] --> position [0,1,2,3,4,5]
### pass 1
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[8,4,23,42,16,15]`
    - j = 0
    - temp = 8
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the while loop, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first
### update [4,8,23,42,16,15] --> position [0,1,2,3,4,5]
### pass 2
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[4,8,23,42,16,15]`
    - j = 1
    - temp = 8
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. we find no values are smaller than `temp`. The minimum value does not change at all during the iteration of this pass
### update [4,8,23,42,16,15] --> position [0,1,2,3,4,5]
### pass 3
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[4,8,23,42,16,15]`
    - j = 2
    - temp = 23
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. we find no values are smaller than `temp`. Both position 4 and 5 are smaller than the value in position 2. Each time a smaller number than `temp` is found, the variable will update to the new smallest number. In this case, 15 is the next smallest number. As a result, it will swap with `j = 2`.
### update [4,8,15,42,16,23] --> position [0,1,2,3,4,5]
### pass 3
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[4,8,15,42,16,23]`
    - j = 3
    - temp = 42
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. we find no values are smaller than `temp`. we find that 16 is the next smallest number in the array, and as a result, switches places with the 42
### update [4,8,15,16,42,23] --> position [0,1,2,3,4,5]
### pass 3
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[4,8,15,16,42,23]`
    - j = 4
    - temp = 42
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. we find no values are smaller than `temp`. we found the array only has one other index to evaluate. Since the last index value is larger than index 4, the two values will swap.
### update [4,8,15,16,23,42] --> position [0,1,2,3,4,5]
### pass 3
- inside the for loop we evaluate the `j` value and the item `temp` value at `j` in the `[4,8,15,16,23,42]`
    - j = 5
    - temp = 42
- while loop if there is a smaller number in the array than what is currently present in `temp` and the `j` value is bigger or equal to zero. we find no values are smaller than `temp`. On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself. After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.
## Efficency
- Time: O(n^2)
    - The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
- Space: O(1)
    - No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

[PR link](https://github.com/HishamKhalil1990/data-structures-and-algorithms/pull/42)

