class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters and len(target) == 1:
            for i in range(len(letters)):
                if ord(letters[i]) > ord(target):
                    return letters[i] 
        return letters[0]
