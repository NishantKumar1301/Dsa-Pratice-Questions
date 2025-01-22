#Question : Crazy Jumping Frogs
#Link to the question: https://www.codechef.com/START170B/problems/FROGS_JUMP

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    even =odd=0
    for num in arr:
        if num %2 ==0:
            even +=1
        else:
            odd+=1
    print(max(even , odd))
