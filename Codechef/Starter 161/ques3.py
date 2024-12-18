#Question : Temporary Temperature
#Link to the question: https://www.codechef.com/problems/TMPTMP 

# cook your dish here
for _ in range(int(input())):
    n , k =map(int,input().split())
    arr= list(map(int,input().split()))
    # arr2 = list(map(int,input().split()))
    mini = arr[0]
    maxi = arr[0]
    for i in arr :
        if i < mini:
            mini =i 
        if i> maxi :
            maxi =i 
    low =0
    high = maxi - mini 
    if high < 0:
        high =0
    while low < high:
        mid = low + (high - low)//2 
        grps =1 
        curr_low =arr[0]-mid
        curr_high = arr[0]+ mid 
        for i in range(1,n):
            new_low = arr[i]-mid
            new_high = arr[i] + mid
            curr_low = max(curr_low,new_low)
            curr_high = min(curr_high,new_high)
            if curr_low > curr_high:
                grps+=1
                curr_low = new_low
                curr_high = new_high
        if grps <= k+1:
            high = mid 
        else:
            low = mid + 1 
    print(low)
            


