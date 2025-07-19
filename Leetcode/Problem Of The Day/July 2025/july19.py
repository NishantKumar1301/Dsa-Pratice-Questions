#Question : Remove Sub-Folders from the Filesystem
#Link to the question: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        ans = [folder[0]]
        for i in range(1, len(folder)):
            last = ans[-1]
            last += "/"
            if not folder[i].startswith(last):
                ans.append(folder[i])
        return ans