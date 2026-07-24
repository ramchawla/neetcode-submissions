class Solution:

    def encode(self, strs: List[str]) -> str:
        # need to provide length, delimiter, followed by string
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + ":" + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # ["5:Hello5:World"]
        # s = "10:helloworld"
        # use 2 pointer approach 
        # use the 3 elements to extract each string
        i = 0
        ans = []

        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length = int(s[i:j])
            tmp = s[j+1:j+1+length]
            ans.append(tmp)
            i = j + 1 + length
        
        return ans