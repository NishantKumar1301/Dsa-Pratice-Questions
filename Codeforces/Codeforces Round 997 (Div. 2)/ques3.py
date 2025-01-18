#Question : Palindromic Subsequence
#Link to the question: https://codeforces.com/contest/2056/problem/C

 
"""Author : Nishant Kumar"""
def main():
    for _ in range(int(input())):
        n = int(input())  
        print("1", end=" ")
        for i in range(2, n - 1):
            print(i - 1, end=" ")
        print("1 2")
 
if __name__ == "__main__":
    main()
 
 
"""Author : Nishant Kumar"""


