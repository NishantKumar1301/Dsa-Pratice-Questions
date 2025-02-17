#Question : Three Activities
#Link to the question: https://codeforces.com/problemset/problem/1914/D

import sys

def max_sum(n, a, b, c):
    # Using sorted lists to simulate multiset-like behavior
    x = sorted([(b[i], i) for i in range(n)], reverse=True)
    y = sorted([(c[i], i) for i in range(n)], reverse=True)

    ans = 0

    for i in range(n):
        # Removing current element
        x_filtered = [pair for pair in x if pair[1] != i]
        y_filtered = [pair for pair in y if pair[1] != i]

        max_x1, idx_x1 = x_filtered[0] if x_filtered else (0, -1)
        max_y1, idx_y1 = y_filtered[0] if y_filtered else (0, -1)

        if idx_x1 == idx_y1:  # If max elements have the same index
            max_x2 = x_filtered[1][0] if len(x_filtered) > 1 else 0
            max_y2 = y_filtered[1][0] if len(y_filtered) > 1 else 0
            ans = max(ans, a[i] + max(max_x2 + max_y1, max_x1 + max_y2))
        else:
            ans = max(ans, a[i] + max_x1 + max_y1)

    return ans

# Fast input reading
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1

results = []
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1 : index + 1 + n]))
    b = list(map(int, data[index + 1 + n : index + 1 + 2 * n]))
    c = list(map(int, data[index + 1 + 2 * n : index + 1 + 3 * n]))
    index += 1 + 3 * n

    results.append(str(max_sum(n, a, b, c)))

sys.stdout.write("\n".join(results) + "\n")
