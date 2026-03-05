import pytest
from test_strings import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

class TestStringUtils:

    @pytest.mark.parametrize("input, expected", [
        ("hello", "olleh"),
        ("",""),
        ("a","a")
    ])
    def test_reverse(self, utils, input, expected):
        assert utils.reverse(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("tuut", True),
        ("test", False),
        ("Racecar", True)
    ])
    def test_palindrome(self,utils, input, expected):
        assert utils.is_palindrome(input) == expected

    # Keep word_count tests as-is for now
    # --- word_count() tests ---

