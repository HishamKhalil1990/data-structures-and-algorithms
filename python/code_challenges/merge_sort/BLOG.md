# Merge Sort
## The original Input
![1](img/1.png)
## The first step
![2](img/2.png)

Here we split the original list into two parts and re-call the merge-sort function again two times. in the first one we pass the list in the right and in the second we pass the the list in the left
## The Second step
![3](img/3.png)

we split both lists from first step into two lists for each and re-call the merge-sort function again. however now we re-call four tims. one call for each list
## The Third step
![4](img/4.png)

we split only lists with more than one value from second step into two lists for each list. now we start passing each right and left form this step and above. the last two splitted lists in this step will start merging because each one has a left and right then each merged list will merge with one from the above level
## The Fourth step
![5](img/5.png)

finally we have two lists as a result from merging from down to above. these two lists will be passed with the original list to be merged into one sorted list
## The Fifth step
![6](img/6.png)

in this step. the two lists from step four merged and sorted into one single list and returned.


### [PR-link](https://github.com/HishamKhalil1990/data-structures-and-algorithms/pull/43)
