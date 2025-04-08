#Question : Simple Repetition
#Link to the question: https://codeforces.com/contest/2093/problem/C

def is_prime(n):
    if n < 2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    x,k = map(int,input().split())
    if k==1:
        if is_prime(x):
            print("Yes")
        else:
            print("NO")
    else:
        if x==1 and k==2:
            print("YES")
        else:
            print("NO")

