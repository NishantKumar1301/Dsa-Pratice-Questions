#Question : Find All Possible Recipes from Given Supplies
#Link to the question: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21

class Solution:
    def findAllRecipes(self,recipes,ingredients,supplies,):
        flag = dict.fromkeys(supplies, True)
        idx = {r: idx for idx, r in enumerate(recipes)}

        def helper(r, visited) :
            if flag.get(r, False):
                return True

            if r not in idx or r in visited:
                return False

            visited.add(r)

            flag[r] = all(
                helper(i, visited)
                for i in ingredients[idx[r]]
            )

            return flag[r]

        return [r for r in recipes if helper(r, set())]

