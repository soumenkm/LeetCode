class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        wordSet = set([beginWord] + wordList)
        Q = deque([(beginWord, 1)])
        wordSet.remove(beginWord)
        res = 0
        while len(Q) != 0:
            word, dist = Q.popleft()
            n = len(word)
            for i in range(n):
                modWords = [word[:i] + c + word[i+1:] for c in chars]
                for mw in modWords:
                    if mw in wordSet:
                        Q.append((mw, dist+1))
                        wordSet.remove(mw)
                        if mw == endWord:
                            res = dist + 1
        return res