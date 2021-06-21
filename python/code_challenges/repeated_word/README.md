# Repeated word
### create a function that can find and return the first repeated word in a lengthy string if it exists or return `False` if it does not
## Whiteboard Process
![ex](img/Untitled.jpg)
## Approach & Efficiency
### i created the function to iterate for each char inside the string to make a word then check if it is inside the hashtable. if it is not it will be added, else -it exists- then it will be returned as the first repeated
Time= O(N^2)
space = O(1)
## Solution
### to find the first repeated word then:
- use the function repated_word as `repated_word(string)`
### to apply tests then:
- use `pytest --verbose  tests/test_repeated_word.py`

### [code](repeated_word.py)
### [PR](https://github.com/HishamKhalil1990/data-structures-and-algorithms/pull/47)
