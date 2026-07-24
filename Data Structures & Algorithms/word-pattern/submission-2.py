class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() # ["dog", "cat", "cat"], "abc"
        if len(words) != len(pattern):
            return False
        dic = {} # {"a": "dog", "b": "cat", }
        for index, letter in enumerate(pattern):
            if letter in dic and dic[letter] == words[index]:
                continue
            elif letter in dic and dic[letter] != words[index]:
                return False
            elif letter not in dic:
                dic[letter] = words[index]
        values = list(dic.values())
        if len(values) != len(set(values)):
            return False
        return True