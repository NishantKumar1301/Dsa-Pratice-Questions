#Question : Minimum Number of People to Teach
#Link to the question: https://leetcode.com/problems/minimum-number-of-people-to-teach/
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        sad_user =set()
        for friend in friendships:
            u= friend[0]-1
            v = friend[1]-1
            s = set(languages[u])
            can_talk = False
            for lang in languages[v]:
                if lang in s:
                    can_talk = True
                    break

            if not can_talk:
                sad_user.add(u)
                sad_user.add(v)

        lang_cnt = [0] *(n+1)
        maxi = 0
        for user in sad_user:
            for lang in languages[user]:
                lang_cnt[lang]+=1
                if lang_cnt[lang]>=maxi:
                    maxi = lang_cnt[lang]
        return len(sad_user)-maxi