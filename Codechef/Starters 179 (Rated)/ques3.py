#Question : Unlock The Safe
#Link to the question: https://www.codechef.com/problems/UNLOCKSAFE

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    cnt = 0
    mini = float('inf')
    
    for i in range(n):
        a = min(abs(arr1[i] - arr2[i]), 9 - abs(arr1[i] - arr2[i]))
        b = max(abs(arr1[i] - arr2[i]), 9 - abs(arr1[i] - arr2[i]))
        cnt += a
        mini = min(mini, b - a)
    
    if cnt <= k:
        if abs(cnt - k) % 2 == 0:
            print("YES")
        else:
            flag = False
            cnt = k - cnt
            if mini <= cnt:
                flag = True
                
            if flag:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")


