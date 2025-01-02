#Question : Count Vowel Strings in Ranges
#Link to the question: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/

class Solution(object):
    def isVowel(self,char):
        vowels ={'a','e','i','o','u'}
        if char in vowels:
            return True
        else:
            return False
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowel_flag =[1 if self.isVowel(word[0]) and self.isVowel(word[-1]) else 0 for word in words]
        prefix_sum =[0]*len(vowel_flag)
        prefix_sum[0]=vowel_flag[0]
        for i in range(1,len(prefix_sum)):
            prefix_sum[i]=prefix_sum[i-1]+vowel_flag[i]
        ans =[]
        for query in queries:
            if query[0]==0:
                ans.append(prefix_sum[query[1]])
            else:
                ans.append(prefix_sum[query[1]]-prefix_sum[query[0]-1])

        return ans


