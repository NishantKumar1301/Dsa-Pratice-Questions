#Question :  Minimum Time to Repair Cars
#Link to the question: https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16


class Solution:
    def repairCars(self, ranks, cars) :
        low, high = 1, cars * cars * ranks[0]

        while low < high:
            mid = (low + high) // 2
            cnt = sum(int((mid / r) ** 0.5) for r in ranks)

            if cnt < cars:
                low = mid + 1
            else:
                high = mid 

        return low