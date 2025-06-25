class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        row_to_look = []
        output = []
        for s in words:
            if s[0].lower() in first_row:
                row_to_look.append(first_row)
            elif s[0].lower() in second_row:
                row_to_look.append(second_row)
            else:
                row_to_look.append(third_row)

        x = 0
        for word in words:
            in_row = True
            for s in word:
                if s.lower() not in row_to_look[x]:
                    in_row = False
                    break
            if in_row:
                output.append(word)
            x += 1

        return output


        