# python_prac
Python : Practice problems for beginners

Q1. Searching for Patterns:
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(pat, txt) that prints all
occurrences of pat[] in txt[]. You may assume that n > m.

Q2. Check if edit distance between two strings is one:
An edit between two strings is one of the following changes.
 Add a character
 Delete a character
 Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit.

Q3. Print list items containing all characters of a given word
There is a list of items. Given a specific word, e.g., "sun", print out all the items in list which
contain all the characters of "sun".
For example if the given word is "sun" and the items are "sunday", "utensils", ""just" and "sss",
then the program should print "sunday" and "utensils".

Q4. Given a string, find its first non-repeating character
Given a string, find the first non-repeating character in it. For example, if input string is
"GeeksQuiz", then output should be 'G'.

Q5. Check if two given strings are isomorphic to each other
Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for
every character of str1 to every character of str2. And all occurrences of every character in 'str1'
map to same character in 'str2'
Examples:
Input: str1 = "aab", str2 = "xxy"
Output: True
'a' is mapped to 'x' and 'b' is mapped to 'y'.
Input: str1 = "aab", str2 = "xyz"
Output: False
One occurrence of 'a' in str1 has 'x' in str2 and other occurrence of 'a' has 'y'.

Q6. Common elements in all rows of a given matrix
Example: Input:
mat[4][5] = [[1, 2, 1, 4, 8],
 [3, 7, 8, 5, 1],
 [8, 7, 7, 3, 1],
 [8, 1, 2, 7, 9], ];
Output:
1 8 or 8 1
8 and 1 are present in all rows.

Q7. Print Matrix Diagonally
Given a 2D matrix, print all elements of the given matrix in diagonal order. For example,
consider the following 5 X 4 input matrix.
 1 2 3 4
 5 6 7 8
 9 10 11 12
 13 14 15 16
 17 18 19 20
Diagonal printing of the above matrix is
 1
 5 2
 9 6 3
 13 10 7 4
 17 14 11 8
 18 15 12
 19 16
 20

Q8. Find the minimum number of swaps needed to make two lists identical. Print
-1 if this is not possible.
Example:
Input: arrA = [3, 6, 4, 8], arrB = [4, 6, 8, 3]
Output: 2
Explanation: swap 4 with 8, arrB = [8, 6, 4, 3]
Swap 8 with 3, arrB = [3, 6, 4, 8]

Q9. In a list of size N, find the smallest sublist whose sum is multiple of N.
Input: arr = [1, 1, 2, 2, 4, 2]
Output: [2 4]
Explanation: Size of list, N = 6 
Following sublists have sum as multiple of N
[1, 1, 2, 2], [2, 4], [1, 1, 2, 2, 4, 2]
The smallest among all is [2 4].

Q10. Find the sum of absolute differences of all pairs in a given list.
Input: arr = [1, 2, 3, 4]
Output: 10
Explanation: |2-1| + |3-1| + |4-1| + |3-2| + |4-2| + |4-3| = 10

Q11. Given a set, we need to find maximum and minimum possible product
among all subsets of the set.
Input: arr = [4, -2, 5]
Output: Maximum product = 20, Minimum product = -40
Explanation: Maximum product is obtained by multiplying 4 5. Minimum product is obtained by
multiplying 4, -2, 5

Q12. Reverse an array in groups of given size
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] k = 3
Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

Q13. Remove minimum number of characters so that two strings become
anagram of each other (anagrams are words that contain the same characters in
different order).
Input: str1 = "bcadeh" str2 = "hea"
Output: 3
Explanation: We need to remove b, c and d from str1.

Q14. Compare two version numbers and print the latest version number. A
version number is a string which looks like a.b.c.d where a, b etc. are numbers,
Input: V1 = “1.0.31”
V2 = “1.0.27”
Output: V1
V1 version is latest (or larger) because V2 < V1

Q15. You are given a string ‘str’, the task is to check that reverses of all possible
substrings of ‘str’ are present in ‘str’ or not.
Input: str = "ab"
Output: False
Explanation: all substrings are "a","b","ab" but reverse of "ab" is not present in str

Q16. Find all unique substrings of an input string and print them in an increasing
order.

Q17. From a list of numbers and another list of characters, print all <number,
character> pairings.
Input: l1 = [1, 2, 3], l2 = [“c”, “e”]
Output: <1,”c”>, <1,”e”>, <2,”c”>, <2,”e”>, <3,”c”>, <3,”e”>.

Q18. From a list of numbers and another list of characters, print all <number,
character> pairings such that in each output pair the number < character’s
ordinal number (position in list).
Input: l1 = [1, 2, 3], l2 = [“c”, “e”]
Output: <1,”e”>

Q19. Read a list of 2D points (x, y coordinates), and find the area of the smallest
(upright) rectangle enclosing all points. (bounded by the smallest and the largest
x and y values).

Q20. Find such smallest area of the rectangle if exactly one point is allowed to
be outside the rectangle.
