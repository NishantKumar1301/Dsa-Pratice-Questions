#Question : Chemistry
#Link to the question: https://codeforces.com/problemset/problem/1883/B
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord('a')] += 1

    odd = sum(1 for count in freq if count % 2 == 1)

    if odd > k + 1:
        print("NO")
    else:
        print("YES")
