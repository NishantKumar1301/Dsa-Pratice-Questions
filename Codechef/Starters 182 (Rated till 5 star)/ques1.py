#Question : Bar Queue
#Link to the question: https://www.codechef.com/START182B/problems/QBGI

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s= input()
    b = g= 0
    for i in range(n):
        if b>2*g:
            break
        if s[i]=='B':
            b+=1
        else:
            g+=1
    print(b+g)

