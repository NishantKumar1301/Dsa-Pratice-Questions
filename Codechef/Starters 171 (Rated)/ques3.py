#Question : WHITEWALL
#Link to the question: https://www.codechef.com/problems/WHITEWALL


# cook your dish here
options = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]
for _ in range(int(input())):
    n = int(input())
    s = input()
    dummy = [0] * 6
    for i in range(n):
        char = s[i]
        for p in range(6):
            expect = options[p][i % 3]
            if char != expect:
                dummy[p] += 1
    
    print(min(dummy))



