def solve():
    low, high = 0, 999
    while low < high:
        mid = low + (high - low) // 2
        print(f"? {mid} {mid}", flush=True)  
        n = int(input())  
        
        if n == mid * mid:
            low = mid + 1  
        else:
            high = mid 
            
    print(f"! {low}")  

for _ in range(int(input())):
    solve()
