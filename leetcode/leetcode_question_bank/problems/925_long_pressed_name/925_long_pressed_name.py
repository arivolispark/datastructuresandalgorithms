class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        result = []
        last_character = typed[0]
        result.append(typed[0]) 

        for i in range(1, len(typed)):
            if typed[i] == last_character:
                continue
            else:
                result.append(typed[i])
                last_character = typed[i]
        
        return True if ''.join(result) == name else False
