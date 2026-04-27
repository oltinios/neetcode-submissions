class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(list(s))
        second = sorted(list(t))
        if len(s) != len(t):
            return False
        if first == second:
            return True
        elif first != second:
            return False
        