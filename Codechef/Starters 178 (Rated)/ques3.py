#Question : Big Difference
#Link to the question: https://www.codechef.com/START178B/problems/BIGDIF

# cook your dish here
def big_difference():
    a,b = map(int, input().split())
    
    if a <= b + 1:
        print(-1, -1)
        return
    
    if a % 2 == 1:
        print(2, a)
        return
    else:
        if a != b + 2:
            print(2, a - 1)
            return
        else:
            print(-1, -1)
            return

for _ in range(int(input())):
    big_difference()


