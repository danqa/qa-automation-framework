import pytest
from test_strings import StringUtils

class TestStringUtils:

    def setup_method(self):
        self.utils = StringUtils()

    # --- reverse() tests ---
    def test_reverse_normal_string(self):
        result = self.utils.reverse("hello")
        assert result == "olleh"

    def test_reverse_empty_string(self):
        result = self.utils.reverse("")
        assert result == ""

    def test_reverse_single_character(self):
        result = self.utils.reverse("a")
        assert result == "a"

    # --- is_palindrome() tests ---
    def test_palindrome_true(self):
        assert self.utils.is_palindrome("racecar")

    def test_palindrome_false(self):
        assert not self.utils.is_palindrome("happy")

    def test_palindrome_mixed_case(self):
        assert self.utils.is_palindrome("Racecar")

    # --- word_count() tests ---
    def test_word_count_normal_sentence(self):
        assert self.utils.word_count("hello world") == 2

    def test_word_count_empty_string(self):
        assert self.utils.word_count("") == 0

    def test_word_count_extra_spaces(self):
        assert self.utils.word_count("  hello   world  ") == 2

    
