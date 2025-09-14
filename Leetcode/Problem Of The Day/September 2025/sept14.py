#Question : Vowel Spellchecker
#Link to the question: https://leetcode.com/problems/vowel-spellchecker/
class Solution(object):
    def __init__(self):
        self.set_ = set()          
        self.casemMap = {}
        self.vowelMap ={}
    
    def maskVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return ''.join('*' if c in vowels else c for c in s)
    
    def checkForMatch(self, query) :
        # Exact match
        if query in self.set_:
            return query
        # Case error match
        lowerQuery = query.lower()
        if lowerQuery in self.casemMap:
            return self.casemMap[lowerQuery]
        # Vowel error match
        maskedQuery = self.maskVowels(lowerQuery)
        if maskedQuery in self.vowelMap:
            return self.vowelMap[maskedQuery]
        # No match
        return ""
    

    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        for word in wordlist:
            self.set_.add(word)
            lowerWord = lower(word)
            if lowerWord not in self.casemMap:
                self.casemMap[lowerWord] = word
            maskedWord = self.maskVowels(lowerWord)
            if maskedWord not in self.vowelMap:
                self.vowelMap[maskedWord] = word
        ans = []
        for query in queries:
            ans.append(self.checkForMatch(query))
        return ans