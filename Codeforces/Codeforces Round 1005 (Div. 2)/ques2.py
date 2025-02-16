#Question : Variety is Discouraged
#Link to the question:  https://codeforces.com/contest/2064/problem/B

##This code gives tle for the larger test case 

# Contest: Codeforces Round 1005 (Div. 2)
# Date: February 16, 2025
# Author: Nishant Kumar
from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    freq = Counter(arr)
    unique = {num for num,count in freq.items()  if count==1}
    l1=r1=-1
    max_length = 0
    left =0
    for right in range(n):
        if arr[right] not in unique:
            left = right+1
        else:
            length = right-left+1
            if length>max_length:
                max_length = length
                l1=left
                r1 = right
    if max_length==0:
        print("0")
    else:
        print(l1+1,r1+1)
 
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar


"""Without tle : java code :

import java.io.*;
import java.util.*;
 
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
 
        StringBuilder result = new StringBuilder();
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[n];
            String[] input = br.readLine().trim().split(" ");
            
            Map<Integer, Integer> freq = new HashMap<>();
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(input[i]);
                freq.put(arr[i], freq.getOrDefault(arr[i], 0) + 1);
            }
 
            int maxLength = 0, l1 = -1, r1 = -1;
            int i = 0;
 
            while (i < n) {
                if (freq.get(arr[i]) == 1) {
                    int start = i + 1;
                    int length = 0;
                    while (i < n && freq.get(arr[i]) == 1) {
                        length++;
                        i++;
                    }
 
                    if (length > maxLength) {
                        maxLength = length;
                        l1 = start;
                        r1 = i;
                    }
                } else {
                    i++;
                }
            }
 
            if (l1 == -1) result.append("0\n");
            else result.append(l1).append(" ").append(r1).append("\n");
        }
        System.out.print(result);
    }
}




"""

