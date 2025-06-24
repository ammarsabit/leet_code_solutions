class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        srted = ['']*len(words)
        for word in words:
            index = int(word[-1])-1
            srted[index] = word[:-1]
        
        return ' '.join(srted)