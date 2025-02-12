#Question : Overwrite
#Link to the question: https://www.codechef.com/problems/MINOVER

# cook your dish here
def main():
    son = int(input())
    while son > 0:
        son -= 1
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        check, ind = float('inf'), -1
        for i in range(m):
            if b[i] < check:
                check = b[i]
                ind = i

        if m == 1:
            print(" ".join(str(min(b[0], a[i])) for i in range(n)))
        else:
            c = [b[(ind + i) % m] for i in range(m)]

            ind1 = -1
            for i in range(n - m + 1):
                if a[i] > check:
                    ind1 = i
                    break

            if ind1 != -1:
                for i in range(ind1, n - m + 1):
                    a[i] = check

            push_ = False
            for i in range(m):
                if a[n - m + i] > c[i]:
                    push_ = True
                    break
                elif a[n - m + i] < c[i]:
                    push_ = False
                    break

            if ind1 != -1 or push_:
                for i in range(m):
                    a[n - m + i] = c[i]

            print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
