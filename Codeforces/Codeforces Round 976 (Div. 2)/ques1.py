#Question : Find Minimum Operations
#Link to the question: https://codeforces.com/contest/2020/problem/A


def largest_power(n, k):
    res = 1
    while res * k <= n:
        res *= k
    return res

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, k = map(int, data[i].split())
        if k == 1:
            results.append(str(n))
        else:
            counter = 0
            while n >= k:
                res = 1
                # Directly compute largest power 
                while res * k <= n:
                    res *= k
                n -= res
                counter += 1
            results.append(str(counter + n))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
