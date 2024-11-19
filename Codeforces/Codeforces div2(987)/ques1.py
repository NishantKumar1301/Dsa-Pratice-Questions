"""#How to Find the element which have the maximum occurence in the array
from collections import Counter
arr =[1,1,22,2,2,2,4,5,6,7,999,9,99,9,9,9,99,2,2]
freq_map = Counter(arr)
max_element= max(freq_map,key = freq_map.get)
print(max_element)"""

#Link to the problem statement : https://codeforces.com/problemset/problem/2031/A
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    freq_map = Counter(arr)
    max_element_occurence = max(x for x in freq_map.values())
    print(n-max_element_occurence)