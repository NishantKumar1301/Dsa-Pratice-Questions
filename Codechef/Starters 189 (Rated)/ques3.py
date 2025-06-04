#Question : Distinct 2 Subarray
#Link to the question: https://www.codechef.com/START189B/problems/DIS2SUB
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    p = n+1
    ans =p 
    for i in range(n):
        freq ,diff= [0] * 101, 0
        for j in range(i, n):
            x = arr[j]
            if freq[x] == 0:
                diff += 1
            freq[x] += 1
            if diff == 2:
                win_length = j - i + 1
                if win_length < ans:
                    ans = win_length
                break
            elif diff > 2:
                break  
    if ans ==p:
        print(-1)
    else:
        print(ans)
