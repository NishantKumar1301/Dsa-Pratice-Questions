#Question : 2Sum
#Link to the question:https://www.naukri.com/code360/problems/reading_6845742?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems

def read(n: int, book, target: int) :
    # Write your code here.
    left = 0
    right = n-1
    book.sort()
    while left<right:
        sum_value = book[left]+book[right]
        if sum_value==target:
            return "YES"
        elif sum_value<target:
            left+=1
        else:
            right-=1
    return "NO"

