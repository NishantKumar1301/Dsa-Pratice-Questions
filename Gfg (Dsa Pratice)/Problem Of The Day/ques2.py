#Question : Anagram
#Link to the question: https://www.geeksforgeeks.org/problems/anagram-1587115620/1

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1)!=len(s2):
            return False
        sorted_s1 = "".join(sorted(s1))
        sorted_s2 = "".join(sorted(s2))
        if sorted_s1 != sorted_s2:
            return False
        return True

