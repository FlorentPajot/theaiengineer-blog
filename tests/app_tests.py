from unittest import TestCase


class BaseClassForTests(TestCase):

    def setUp(self):
        self.foo = None


class FakeTEest(BaseClassForTests):

    def test_fake(self):
        self.assertTrue(self.foo is None)
