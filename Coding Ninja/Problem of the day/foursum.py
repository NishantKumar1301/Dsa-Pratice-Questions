#Question : 4Sum
#Link to the question: https://www.naukri.com/code360/problems/4sum_5713771?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems&leftPanelTabValue=PROBLEM

def fourSum(nums: [int], target: int) -> [[int]]:
    # Write your code from here.
    ans =[]
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j!=i+1 and nums[j]==nums[j-1]:
                continue 
            k = j+1
            l=n-1
            while k<l:
                total = nums[i]+nums[j]+nums[k]+nums[l]
                if total<target:
                    k+=1
                elif total>target:
                    l-=1
                else:
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    ans.append(temp)
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1

    return ans


