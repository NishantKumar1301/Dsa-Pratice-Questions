#Question : Hamming equivalent
#Link to the question: https://www.codechef.com/problems/P4169

# cook your dish here
def count_permutation(a):
    return [bin(num).count('1') for num in a]

def helper_ques2(n, num):
    arr = count_permutation(num)
    for i in range(n):
        if arr[i] != bin(i + 1).count('1'):
            return "No"
    return "Yes"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(helper_ques2(n, arr))



