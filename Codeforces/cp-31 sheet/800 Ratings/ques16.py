#Question : Desorting
#Link to the question: https://codeforces.com/contest/1853/problem/A


def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split())) 
        
        ans = float('inf') 
        for i in range(n - 1):
            if a[i] <= a[i + 1]: 
                diff = a[i + 1] - a[i]  
                req = diff // 2 + 1  
                ans = min(ans, req)  
            else:  
                ans = 0
        
        print(ans)  

if __name__ == "__main__":
    main()