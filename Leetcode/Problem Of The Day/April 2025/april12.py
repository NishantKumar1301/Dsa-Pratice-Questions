#Question : Find the Count of Good Integers
#Link to the question: https://leetcode.com/problems/find-the-count-of-good-integers/description/?envType=daily-question&envId=2025-04-12

class Solution(object):
    def __init__(self):
        self.ans=0
        self.visited= set()
        self.fact = [0]*11

    def calculate_factorial(self,n):
        self.fact[0]=self.fact[1]=1
        for i in range(2,11):
            self.fact[i] = i*self.fact[i-1]

    def count_permutation(self,n,freq):
        cnt = self.fact[n]
        for i in range(10):
            cnt=cnt//self.fact[freq[i]]
        return cnt

    def all_arrangement(self,number,n):
        sorted_num = ''.join(sorted(number))
        num = int(sorted_num)
        if num in self.visited:
            return 0
        self.visited.add(num)
        freq =[0]*10
        for char in sorted_num:
            freq[int(char)]+=1
        total_permutation = self.count_permutation(n,freq)
        invalid =0
        if freq[0]>0:
            freq[0]-=1
            invalid = self.count_permutation(n-1,freq)
        return total_permutation-invalid

    def is_k_palindrome(self,num,k):
        return int(num)%k==0

    def generate_palindrome(self,pos,n,num,k):
        if pos>=(n+1)//2:
            num_str = ''.join(num)
            if self.is_k_palindrome(num_str,k):
                self.ans+=self.all_arrangement(num_str,n)
            return 
        start ='1' if pos ==0 else '0'
        for c in range(ord(start),ord('9')+1):
            num[pos]=chr(c)
            num[n-pos-1]=chr(c)
            self.generate_palindrome(pos+1,n,num,k)
        num[pos]=' '

    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.calculate_factorial(n)
        num = [' ']*n
        self.generate_palindrome(0,n,num,k)
        return self.ans
