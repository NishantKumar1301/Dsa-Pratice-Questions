#Question : Bitwise Balancing
#Link to the question: https://codeforces.com/contest/2020/problem/C

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])

    mp = {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (0, 1, 0): 0,
        (0, 1, 1): -1,
        (1, 0, 0): -1,
        (1, 0, 1): 0,
        (1, 1, 0): 1,
        (1, 1, 1): 0,
    }

    # Process each test case
    results = []
    for idx in range(1, t + 1):
        a = 0
        b, c, d = map(int, data[idx].split())

        for i in range(60, -1, -1):
            I = (b >> i) & 1
            J = (c >> i) & 1
            K = (d >> i) & 1
            X = mp[(I, J, K)]

            if X == -1:
                a = -1
                break
            else:
                a += X * (1 << i)

        results.append(str(a))

    # Print all results
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()

