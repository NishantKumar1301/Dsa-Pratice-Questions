#Question : Continuous Subarrays
#Link to the question: https://leetcode.com/problems/continuous-subarrays/description/?envType=daily-question&envId=2024-12-14

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = right = ans = 0
        maxi = float('-inf')
        mini = float('inf')
        for right in range(n):
            maxi = max(maxi,nums[right])
            mini = min(mini,nums[right])

            #If the maxi-mini >2 then compress the window

            if maxi- mini > 2:
                #window size = right - left
                win_size = right - left
                #If length = n then total number of subarray = (n*(n+1))//2
                ans += (win_size*(win_size + 1))//2

                #Expand the window as much left is possible
                left = right
                maxi = mini = nums[right]
                while (left > 0 and abs(nums[right]-nums[left-1])<=2):
                    left-=1
                    maxi = max(maxi,nums[left])
                    mini = min(mini,nums[left])

                #Subtract the overlapping interval
                if left<right:
                    win_size = right - left
                    ans -= (win_size*(win_size+1))//2
                
        #Add subarray from the last window
        win_size = n - left
        ans+=(win_size*(win_size+1))//2
        return ans
