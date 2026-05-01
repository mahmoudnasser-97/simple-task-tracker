import unittest
from app import task_tracker

class TestApp(unittest.TestCase):
    def test_task_tracker(self):
        result = task_tracker()
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
