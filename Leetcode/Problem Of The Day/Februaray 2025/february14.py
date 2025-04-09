#Question : https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14
#Link to the question: Product of the Last K Numbers


class ProductOfNumbers:
    def __init__(self):
        self.arr = [1] 
        self.idx = 1  
        self.last_zero_idx = -1 

    def add(self, num) :
        if num == 0:
            self.last_zero_idx = self.idx  
            self.arr.append(1) 
        else:
            self.arr.append(self.arr[-1] * num)
        self.idx += 1

    def getProduct(self, k) :
        if self.last_zero_idx >= self.idx - k:  
            return 0  
        return self.arr[self.idx - 1] // self.arr[self.idx - k - 1]

# Example usage:
# obj = ProductOfNumbers()
# obj.add(3)
# obj.add(2)
# obj.add(5)
# param_2 = obj.getProduct(2)  # Should return 10 (2 * 5)
# obj.add(0)  # Resets the product
# param_3 = obj.getProduct(1)  # Should return 0