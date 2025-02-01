#Question :Black Circles
#Link to the question: https://codeforces.com/contest/2002/problem/C

for _ in range(int(input())):
    n = int(input())
    x_ordinate =[]
    y_ordinate = []
    for _ in range(n):
        x,y = map(int,input().split())
        x_ordinate.append(x)
        y_ordinate.append(y)
    x1,y1,x2,y2=map(int,input().split())
    t = (x2-x1)**2+(y2-y1)**2
    for i in range(n):
        d= (x_ordinate[i]-x2)**2+(y_ordinate[i]-y2)**2
        if d<=t:
            print("NO")
            break
        
    else:  
        print("YES")
        

