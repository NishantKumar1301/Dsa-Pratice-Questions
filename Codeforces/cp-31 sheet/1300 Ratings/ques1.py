#Question : Sort the Array
#Link to the question: https://codeforces.com/contest/451/problem/B

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    temp =arr[:]
    arr.sort()
    first = second=-1
    for i in range(n):
        if arr[i]!=temp[i]:
            if first ==-1:
                first=i
            second = i+1
    
    if first!=-1 and second!=-1:
        temp[first:second]=reversed(temp[first:second])
    
    if temp==sorted(temp):
        print("yes")
        if first==-1:
            first=0
        if second==-1:
            second = 1
        print(first+1,second)
    else:
        print("no")


if __name__ == "__main__":
    solve()


