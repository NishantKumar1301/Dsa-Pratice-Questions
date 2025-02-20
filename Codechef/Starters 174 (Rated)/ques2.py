#Question : Bigger is Better
#Link to the question: https://www.codechef.com/problems/BIGNAME

def solve(A, N):
    for c in range(ord('a'), ord('z') + 1):
        can = chr(c) * N
        rev = can[::-1]

        if can > A and rev > A:
            return can

    return "-1"

def main():
    for _ in range(int(input().strip())):
        n = int(input().strip())  
        s = input().strip()      
        print(solve(s, n))       

if __name__ == "__main__":
    main()
