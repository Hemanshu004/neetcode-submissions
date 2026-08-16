class Solution:
    def check(self, s1, s2):
        length = min(len(s1), len(s2))
        n = 0

        for i in range(length):
            if s1[i] != s2[i]:
                n += 1

            if n > 1:
                break

        return n == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        wordList.append(beginWord)

        for ch in wordList:
            for j in range(len(ch)):
                pattern = ch[:j] + "*" + ch[j+1:]
                adj[pattern].append(ch)

        q = deque()
        visit = set()

        q.append((beginWord, 1))
        visit.add(beginWord)

        while q:
            node, steps = q.popleft()

            if node == endWord:
                return steps

            for j in range(len(node)):
                pattern = node[:j] + "*" + node[j+1:]

                for nei in adj[pattern]:
                    if nei not in visit:
                        q.append((nei, steps + 1))
                        visit.add(nei)

        return 0