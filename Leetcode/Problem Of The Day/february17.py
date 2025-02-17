#Question : Letter Tile Possibilities
#Link to the question: https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17

class Solution(object):
    def build(self,freq):
        ways =0
        for i in range(26):
            if freq[i]>0:
                freq[i]-=1
                ways +=1+self.build(freq)
                freq[i]+=1
        return ways
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :r type: int
        """
        freq=[0]*26
        for tile in tiles:
            freq[ord(tile)-ord('A')]+=1
        return self.build(freq)
        