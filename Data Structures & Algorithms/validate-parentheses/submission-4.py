class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s:
            if char in matching:
                stack.append(matching[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return len(stack) == 0