# Testing frameworks return exit code 5 in case there is no tests, placeholder avoid CI tools to see as error.
from unittest import TestCase


class TestPlaceholder(TestCase):
    def test_placeholder(self) -> None:
        pass
