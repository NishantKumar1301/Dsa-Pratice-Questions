#Question : Target Pratice
#Link to the question: https://codeforces.com/problemset/problem/1873/C

score =[
    [1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1],
]

def solve():
    arr=[]
    for _ in range(10):
        row = input().strip()
        arr.append(row)
    # Write your logic here
    ans =0
    for i in range(10):
        for j in range(10):
            if arr[i][j]=='X':
                ans += score[i][j]
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
