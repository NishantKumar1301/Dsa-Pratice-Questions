#Question : Word Ladder
#Link to the question: https://leetcode.com/problems/word-ladder/description/
from collections import deque
class Solution(object):
    def ladderLength(self, start, end, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = deque()
        queue.append((start,1))
        s = set(wordList)
        if start in s:
            s.remove(start)
        while queue:
            word,step = queue.popleft()
            if word==end:
                return step
            for i in range(len(word)):
                org_char = word[i]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    word = word[:i]+char+word[i+1:]
                    if word in s:
                        s.remove(word)
                        queue.append((word,step+1))
                word = word[:i]+org_char+word[i+1:]
        return 0

