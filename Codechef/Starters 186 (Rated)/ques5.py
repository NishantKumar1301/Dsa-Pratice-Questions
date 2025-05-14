#Question : Best Movie
#Link to the question: https://www.codechef.com/START186B/problems/BESTMOVIE

for _ in range(int(input())):
    n = int(input())
    mini = float('inf')
    for _ in range(n):
        a, b = map(int, input().split())
        if a >= 7 and b < mini:
            mini = b
    print(mini if mini != float('inf') else -1)


