# Question: Replace Character
# Link to the question: https://codeforces.com/contest/2047/problem/B

"""Author : Nishant Kumar"""

"""
The total number of permutations of a string can be calculated using the formula:
n! / (a! * b! * c! * ...), where:
- n is the total length of the string.
- a, b, c, ... are the occurrences of each unique character in the string.

Since the length of the string (n) does not change, the numerator (n!) remains constant.
To minimize the total number of permutations, we need to maximize the denominator 
(a! * b! * c! * ...). This can be achieved by increasing the frequency of one character 
while decreasing the diversity of distinct characters.

Steps to achieve the minimal number of permutations:
1. Identify the character with the **lowest frequency** (smallest occurrence).
2. Identify the character with the **highest frequency** (largest occurrence).
3. Replace the first occurrence of the character with the smallest frequency 
   with the character having the largest frequency.

This operation:
- Increases the frequency of the most frequent character.
- Decreases the number of distinct characters.
- Maximizes the denominator, thereby minimizing the total number of permutations.

By applying this transformation, the string's arrangement results in the fewest possible
distinct permutations, meeting the problem's requirements.
"""


def solve():
    n = int(input())
    s = input().strip()
    
    # Put all the characters with their count in a dictionary
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1 
            
    # Find the maximum and minimum occurred character
    mini = maxi = s[0]
    for char in freq:
        if freq[char] > freq[maxi] or (freq[char] == freq[maxi] and char > maxi):
            maxi = char
        if freq[char] < freq[mini] or (freq[char] == freq[mini] and char < mini):
            mini = char
    
    # Replace the first occurrence of `mini` with `maxi`
    # Convert the string to a list for mutability
    s = list(s)
    for i in range(n):
        if s[i] == mini:
            s[i] = maxi
            break
    
    # Output the modified string
    print("".join(s))


# Handle multiple test cases
for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""
