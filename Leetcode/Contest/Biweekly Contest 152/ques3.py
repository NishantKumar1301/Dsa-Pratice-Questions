#Question : Longest Common Prefix of K Strings After Removal
#Link to the question: https://leetcode.com/contest/biweekly-contest-152/problems/longest-common-prefix-of-k-strings-after-removal/?slug=design-spreadsheet&region=global_v2

class SegmentTree:
    def __init__(self, n, cnt_g):
        self.n = n
        self.cnt_g = cnt_g
        self.tree = [-1] * (4 * (n + 1))
        self.build(1, 1, n)

    def build(self, idx, l, r):
        if l == r:
            self.tree[idx] = l if self.cnt_g[l] > 0 else -1
            return
        mid = (l + r) // 2
        self.build(idx * 2, l, mid)
        self.build(idx * 2 + 1, mid + 1, r)
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def update(self, idx, l, r, pos, new_val):
        if l == r:
            self.tree[idx] = l if new_val > 0 else -1
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(idx * 2, l, mid, pos, new_val)
        else:
            self.update(idx * 2 + 1, mid + 1, r, pos, new_val)
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def query(self):
        return self.tree[1]


class Solution:
    def longestCommonPrefix(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[int]
        """
        n = len(words)
        ans = [0] * n
        if n - 1 < k:
            return ans

        arr1 = list(words)

        class TrieNode:
            def __init__(self):
                self.count = 0
                self.depth = 0
                self.children = {}

        trie = [TrieNode()]

        for w in words:
            cur = 0
            for c in w:
                if c not in trie[cur].children:
                    trie[cur].children[c] = len(trie)
                    trie.append(TrieNode())
                    trie[-1].depth = trie[cur].depth + 1
                cur = trie[cur].children[c]
                trie[cur].count += 1

        maxi = 0
        for node in trie[1:]:
            if node.count >= k:
                maxi = max(maxi, node.depth)

        cnt_g = [0] * (maxi + 1)
        for node in trie[1:]:
            if node.count >= k:
                d = node.depth
                if d <= maxi:
                    cnt_g[d] += 1

        arr = [[] for _ in range(n)]
        for i in range(n):
            cur = 0
            for c in words[i]:
                cur = trie[cur].children[c]
                if trie[cur].count == k:
                    arr[i].append(trie[cur].depth)

        si = maxi
        if si >= 1:
            seg_tree = SegmentTree(si, cnt_g)
            for i in range(n):
                if n - 1 < k:
                    ans[i] = 0
                else:
                    for d in arr[i]:
                        seg_tree.update(1, 1, si, d, cnt_g[d] - 1)
                    res = seg_tree.query()
                    ans[i] = 0 if res == -1 else res
                    for d in arr[i]:
                        seg_tree.update(1, 1, si, d, cnt_g[d])
        else:
            ans = [0] * n

        return ans

