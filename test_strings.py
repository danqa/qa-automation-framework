# string_utils.py
class StringUtils:
    def reverse(self, s):
        return s[::-1]

    def is_palindrome(self, s):
        s = s.lower().strip()
        return s == s[::-1]

    def word_count(self, s):
        if not s.strip():
            return 0
        return len(s.split())
