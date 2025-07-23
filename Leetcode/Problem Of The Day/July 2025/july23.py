#Question : Maximum Score From Removing Substrings
#Link to the question: https://leetcode.com/problems/maximum-score-from-removing-substrings

class Solution(object):
    def remove_substring(self,s,matched):
        stack = []
        for char in s:
            if stack and char==matched[1] and stack[-1]==matched[0]:
                stack.pop()
            else:
                stack.append(char)
        new_string = ""
        while stack:
            new_string+= stack.pop()
        return new_string[::-1]
        # return ''.join(stack)

    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        max_str = "ab" if x>y else "ba"
        min_str = "ba" if max_str =="ab" else "ab"
        #Pass 1 
        first_string = self.remove_substring(s,max_str)
        char_removed = n - len(first_string)
        first_pass_pair_removed = char_removed//2
        ans += first_pass_pair_removed* max(x,y)

        #Pass 2 
        second_string = self.remove_substring(first_string,min_str)
        char_removed = len(first_string) - len(second_string)
        second_time_pair_removed = char_removed //2 
        ans += second_time_pair_removed * min(x,y)

        return ans