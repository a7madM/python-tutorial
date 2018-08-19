import unittest
from ..src import RunnerUp
# from Models.user import User

class TestRunnerUp(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( 12, 12)

if __name__ == '__main__':
    unittest.main()