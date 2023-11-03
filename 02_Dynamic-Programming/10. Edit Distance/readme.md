## Edit Distance
Given two strings ```word1``` and ```word2```, return the minimum number of operations required to convert ```word1``` to ```word2```.
You have the following three operations permitted on a word: \
Insert a character\
Delete a character\
Replace a character
```python
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```
[LeetCode Problem Statement](https://leetcode.com/problems/edit-distance/)  \
[Solution using DP](https://github.com/SamirPaulb/DSAlgo/blob/main/02_Dynamic-Programming/10.%20Edit%20Distance/03.%20Edit%20Distance%20Tabular%20DP.py)

[PDF📚](https://github.com/SamirPaulb/assets/blob/main/edit-distance.pdf)
<a href="#"><img src="https://raw.githubusercontent.com/SamirPaulb/assets/main/edit-distance_1.jpg" /></a>
<a href="#"><img src="https://raw.githubusercontent.com/SamirPaulb/assets/main/edit-distance_2.jpg" /></a>
<a href="#"><img src="https://raw.githubusercontent.com/SamirPaulb/assets/main/edit-distance_3.jpg" /></a>
