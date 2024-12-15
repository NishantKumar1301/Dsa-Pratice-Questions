#Question : Insane Problem
#Link to the question: https://codeforces.com/contest/2044/problem/E

for _ in range(int(input())):
    b, left_x, right_x, left_y, right_y = map(int, input().split())
    ans = 0
    
    if b != 1:
        curr = 1
        while curr <= right_y // max(1, left_x):
            if curr != 0:
                lower_x = max(left_x, (left_y + curr - 1) // curr)
            else:
                lower_x = left_x
            
            if curr != 0:
                upper_x = min(right_x, right_y // curr)
            else:
                upper_x = right_x
            
            if lower_x <= upper_x:
                ans += (upper_x - lower_x + 1)
            
            if curr > right_y // b:
                break
            curr *= b
    else:
        low = max(left_x, left_y)
        up = min(right_x, right_y)
        if low <= up:
            ans = up - low + 1
    
    print(ans)

