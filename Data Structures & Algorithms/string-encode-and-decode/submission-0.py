class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + '#' +s for s in strs )

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s)-1:
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            start = j+1
            end = start + length
            word = s[start:end]
            result.append(word)
            i=end
        return result
