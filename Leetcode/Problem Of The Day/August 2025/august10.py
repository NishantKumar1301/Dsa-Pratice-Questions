#Question : Reordered Power of 2
#Link to the question: https://leetcode.com/problems/reordered-power-of-2
class Solution(object):
    def precompute_power(self,set_):
        #Constraint is till 2^29
        for p in range(30):
            power = 1<<p # power of p = 1<<p
            power = str(power)
            sorted_power = sorted(power)
            s = "".join(sorted_power)
            set_.add(s)

    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_ = set()
        self.precompute_power(set_)
        s = "".join(sorted(str(n)))
        return True if s in set_ else False