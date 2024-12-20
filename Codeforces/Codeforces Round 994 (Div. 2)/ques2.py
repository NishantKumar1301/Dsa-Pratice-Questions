#Question : pspspsps
#Link to the question: https://codeforces.com/contest/2049/problem/B

def solve():
    n = int(input())
    word = input()
    freq ={}
    
    #Store the character and its count in the dictionary 
    for char in word:
        freq[char]=freq.get(char,0)+1
    
    #Observation : If the string starts with s and total number of s is 1 then the output is YES
    #If the string ends with p and the total number of p is 1 Then the output is Yes 
    
    if (word[0]=='s' and freq['s']==1) or (word[-1]=='p' and freq['p']==1):
        print("YES")
        return 
        
    #If there is only one type of character then answer is always Yes
    if len(freq)==1:
        print("YES")
        return
    
    #If 2 types of character are present in the string and one of them is . then answer is YES
    if len(freq)==2:
        if '.' in freq:
            print("YES") 
            return
    
    #For the conflicting case ,from the rest cases answer is NO
    print("NO")

for _ in range(int(input())):
    solve()