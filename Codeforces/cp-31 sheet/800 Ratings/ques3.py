#Question : Cover in Water
#Link to the question: https://codeforces.com/problemset/problem/1900/A


def solve():
    n = int(input())
    s= input().strip()
    # Write your logic here
    flag =False
    cnt = 0
    for i in range(n):
        if s[i]=='.' and i+1<n and s[i+1]=='.'and i+2<n and s[i+2]=='.':
            flag = True
            break
        if s[i]=='.':
            cnt+=1
    if flag:
        print(2)
    else:
        print(cnt)



if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
