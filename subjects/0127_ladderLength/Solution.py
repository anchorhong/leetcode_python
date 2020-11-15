from typing import List
from collections import deque
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0



if __name__ == "__main__":
    # beginWord = "qa"
    # endWord = "sq"
    # wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb",
    #             "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br",
    #             "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr",
    #             "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh",
    #             "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb",
    #             "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz",
    #             "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
    #             "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
    #             "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
    #             "pa", "he", "lr", "sq", "ye"]
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
