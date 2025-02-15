#Question : Swap and Delete 
#Link to the question: https://codeforces.com/contest/1913/problem/B


def solve():
    s = input().strip()
    n = len(s)
    count_0,count_1=s.count('0'),s.count('1')
    cnt = [count_0,count_1 ]

    for i in range(n):
        req = 1 - int(s[i])  
        if cnt[req] == 0:
            print(n - i)
            return
        cnt[req] -= 1  

    print(0)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()