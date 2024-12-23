# Question : Swap Columns and Find a Path
# Link to the question: https://codeforces.com/contest/2047/problem/C

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # Combine the arrays into pairs and sort by the difference (arr1[i] - arr2[i]) in descending order
    pairs = list(zip(arr1, arr2))
    pairs.sort(key=lambda x: x[0] - x[1], reverse=True)

    ans = float('-inf')  
    for i in range(n):
        # Calculate the initial sum with the current pair as primary
        total_sum = pairs[i][0] + pairs[i][1]
        for j in range(n):
            if i != j:  # Add the second value (arr2[j]) of all other pairs
                total_sum += pairs[j][1]

        ans = max(ans, total_sum)  # Update the maximum answer

        # Try swapping the first value (arr1[j]) for other pairs
        current_sum = total_sum
        for j in range(n):
            if i != j:
                current_sum -= pairs[j][1]
                current_sum += pairs[j][0]
                ans = max(ans, current_sum)

    print(ans)

for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""
