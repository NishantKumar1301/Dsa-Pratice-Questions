#Question : Accounts Merge
#Link to the question:  https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
class Solution(object):
    def findParent(self,u,parent):
        if parent[u]!=u:
            parent[u]=self.findParent(parent[u],parent)
        return parent[u]
    
    def unionbySize(self,u,v,parent,size):
        pu,pv= self.findParent(u,parent) , self.findParent(v,parent)
        if pu==pv:
            return
        if size[pu]<size[pv]:
            parent[pu]=pv
            size[pv]+=size[pu]
        else:
            parent[pv]=pu
            size[pu]+=size[pv]

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        parent = list(range(n))
        size = [1]*n
        email_to_idx ={}
        
        #Step1 : Union the account that share same email
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email in email_to_idx:
                    self.unionbySize(i,email_to_idx[email],parent,size)
                else:
                    email_to_idx[email]=i
        
        #Step2 : Group the email with their parent
        idx_to_email = defaultdict(list)
        for email,idx in email_to_idx.items():
            root = self.findParent(idx,parent)
            idx_to_email[root].append(email)
        
        #Step 3 : Build the result
        ans = []
        for idx,emails in idx_to_email.items():
            name = accounts[idx][0]
            ans.append([name]+sorted(emails))
        
        return ans
        