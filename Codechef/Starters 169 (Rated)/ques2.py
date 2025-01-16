#Question :Opposite Attract
#Link to the question: https://www.codechef.com/problems/P2169

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = ''.join('1' if char == '0' else '0' for char in s)
    print(ans)


