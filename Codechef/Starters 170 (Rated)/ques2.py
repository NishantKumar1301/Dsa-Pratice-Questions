#Question : Minimum Bottles
#Link to the question: https://www.codechef.com/START170B/problems/MINBOTTLES

# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int, input().split()))
    total = sum(arr)
    print((total+x-1)//x)


