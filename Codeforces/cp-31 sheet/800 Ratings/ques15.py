#Question : United We Stand
#Link to the question: https://codeforces.com/problemset/problem/1859/A

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    a,b =[],[]
    maxi,mini = max(arr),min(arr)
    if maxi ==mini:
        print(-1)
        return
    for num in arr:
        if num==maxi:
            b.append(num)
        else:
            a.append(num)
    print(len(a),len(b))
    print(*a)
    print(*b)



if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
