#Question : 3Sum
#Link to the question: https://www.naukri.com/code360/problems/three-sum_6922132?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems


def triplet(n: int, arr: [int]) -> [[int]]:
    # Write your code here.
    ans =[]
    arr.sort()
    for i in range(n):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        j =i+1
        k=n-1
        while j<k:
            total = arr[i]+arr[j]+arr[k]
            if total<0:
                j+=1
            elif total>0:
                k-=1
            else:
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while j<k and arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+1]:
                    k-=1

    return ans
