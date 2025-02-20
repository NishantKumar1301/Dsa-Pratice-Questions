#Question : Deletion and difference
#Link to the question: https://www.codechef.com/problems/DELDIF

# cook your dish here
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for n in arr:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    z = 0
    c = 0
    for key, count in freq.items():
        if key == 0:
            z += count
            continue
        if count > 1:
            if count % 2 == 0:
                z += count // 2
            else:
                z += count // 2 + 1
                c += 1
        else:
            c += 1

    if z == 0:
        z = 0
    else:
        z = 1
    ans = c+z
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

