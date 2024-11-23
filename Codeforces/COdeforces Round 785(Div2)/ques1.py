#Question : Subtle Substring Subtraction
#Link to the question:  https://codeforces.com/contest/1673/problem/A

for _ in range(int(input())):
    s = input()
    scores =[ord(char)-ord('a')+1 for char in s]
    n = len(s)
    total = sum(scores)
    if n %2 == 0:
        alice = total
        bob =0
        print(f"Alice {alice}")
    else:
        if n ==1:
            alice = 0
            bob =total
            print(f"Bob {bob}")
        else:
            zero_index_sum = sum(scores[0:-1])
            one_index_sum = sum(scores[1:])
            alice = max(zero_index_sum,one_index_sum)
            bob = total - alice
            if alice > bob:
                print(f"Alice {alice-bob}")
            else:
                print(f"Bob {bob-alice}")