#Question : Minimum Colours (Easy)
#Link to the question: https://www.codechef.com/START178B/problems/MINCOL

# cook your dish here
INFINITY = 1000000000

def main():
    
    for _ in range(int(input())):
        n = int(input())
        
        arr = [0] + list(map(int, input().split()))
        
        dp = [0] * (n + 1)
        
        b1 = dp[0]
        b0 = INFINITY
        b = [INFINITY] * (n + 1)
        
        for i in range(1, n + 1):
            if arr[i] == 0:
                b0 = min(b0, dp[i - 1])
            else:
                b[arr[i]] = min(b[arr[i]], dp[i - 1])
            
            b1 = min(b1, dp[i - 1])
            
            if arr[i] == 0:
                dp[i] = 1 + b1
            else:
                c = b0
                c = min(c, b[arr[i]])
                dp[i] = 1 + c
        
        print(dp[n])

if __name__ == "__main__":
    main()


