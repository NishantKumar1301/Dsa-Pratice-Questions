#Question : Doremy's Paint 3
#Link to the question: https://codeforces.com/problemset/problem/1890/A

from collections import defaultdict
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    freq = defaultdict(int)
    for num in arr:
        freq[num]+=1
    if len(freq)>2:
        print("NO")
        return
    freq_list = list(freq.values())
    freq1 = freq_list[0]
    freq2 =freq_list[-1]
    if freq1 ==freq2:
        print("YES")
    elif n%2==1 and abs(freq2-freq1)==1:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
