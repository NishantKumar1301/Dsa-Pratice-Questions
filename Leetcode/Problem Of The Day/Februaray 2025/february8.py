#Question : Design a Number Container System
#Link to the question: https://leetcode.com/problems/design-a-number-container-system/description/?envType=daily-question&envId=2025-02-08

from sortedcontainers import SortedSet
class NumberContainers(object):

    def __init__(self):
        self.index_number ={}
        self.number_index={}

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :r type: None
        """
        if index in self.index_number:
            old_number = self.index_number[index]
            self.number_index[old_number].discard(index)
            if not self.number_index[old_number]:
                del self.number_index[old_number]
        self.index_number[index]=number
        if number not in self.number_index:
            self.number_index[number]=SortedSet()
        self.number_index[number].add(index)


    def find(self, number):
        """
        :type number: int
        :r type: int
        """
        if number not in self.number_index:
            return -1
        return self.number_index[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)