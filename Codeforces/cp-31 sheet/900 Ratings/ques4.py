#Question : Forked
#Link to the question: https://codeforces.com/problemset/problem/1904/A
dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    kx, ky = map(int, input().split())
    qx, qy = map(int, input().split())
    
    king = set()
    queen = set()

    for j in range(4):
        king.add((kx + dx[j] * a, ky + dy[j] * b))
        king.add((kx + dx[j] * b, ky + dy[j] * a))

        queen.add((qx + dx[j] * a, qy + dy[j] * b))
        queen.add((qx + dx[j] * b, qy + dy[j] * a))

    ans = sum(1 for pos in king if pos in queen)
    print(ans)
