#Question : SWISH GAME
#Link to the question: https://www.codechef.com/problems/SWISHGAME

# cook your dish here
for _ in range(int(input())):
    m,k = map(int,input().split())
    s= input()
    cnt = s.count('S')
    if cnt>=k:
        print(m)
    else:
        print(m+k-cnt-1)


