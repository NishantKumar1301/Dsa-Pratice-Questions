#Question :Minimize XOR
#Link to the question: https://leetcode.com/problems/minimize-xor/?envType=daily-question&envId=2025-01-15


class Solution(object):
    
    # Method 1: Check whether a specific bit is set (1) in a number.
    def is_set(self, x, bit):
        return x & (1 << bit) != 0
    
    # Method 2: Set a specific bit in a number (make it 1).
    def set_bit(self, x, bit):
        return x | (1 << bit)
    
    # Method 3: Unset a specific bit in a number (make it 0).
    def unset_bit(self, x, bit):
        return x & ~(1 << bit)

    def minimizeXor(self, num1, num2):
        """
        Minimize the XOR of `num1` by adjusting its bits to match the number 
        of set bits in `num2`.
        """
        ans = num1
        required_set_bit = bin(num2).count('1')
        current_set_bit = bin(num1).count('1')
        bit = 0  # Tracks the current bit position being processed.

        # Case 1: If `current_set_bit` is less than `required_set_bit`,
        # set additional least significant bits (LSBs) in `ans`.
        if current_set_bit < required_set_bit:
            while current_set_bit < required_set_bit:
                if not self.is_set(ans, bit):
                    ans = self.set_bit(ans, bit)
                    current_set_bit += 1
                bit += 1
        
        # Case 2: If `current_set_bit` is greater than `required_set_bit`,
        # unset the most significant bits (MSBs) in `ans` to match the requirement.
        elif current_set_bit > required_set_bit:
            while current_set_bit > required_set_bit:
                if self.is_set(ans, bit):
                    ans = self.unset_bit(ans, bit)
                    current_set_bit -= 1
                bit += 1

        return ans
