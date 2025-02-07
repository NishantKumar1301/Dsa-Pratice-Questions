#Question :  Triple Operations
#Link to the question: https://codeforces.com/contest/1999/problem/E

def compute_step(n):
    step =0
    while n:
        step +=1
        n= n//3
    return step

max_n = int(3e5)
prefix_arr =[0]*max_n
prefix_arr[1]=1
for i in range(2,max_n):
    prefix_arr[i]=prefix_arr[i-1]+compute_step(i)

for _ in range(int(input())):
    l,r = map(int,input().split())
    ans = compute_step(l)*2 +prefix_arr[r]-prefix_arr[l]
    print(ans)