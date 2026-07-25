class Solution:

    def encode(self, strs: List[str]) -> str:
        # "5#Hello5#World"
        encoded_str = ""
        for word in strs:
            length = str(len(word)) + "#"
            # add the length of the string and a separating character
            encoded_str += length
            # add the actual word
            encoded_str += word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        # "5#Hello5#World"
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            i += 1
            length = int(count)
            word = ""
            while length > 0:
                word += s[i]
                i += 1
                length -= 1

            decoded_strs.append(word)
        
        return decoded_strs


            

