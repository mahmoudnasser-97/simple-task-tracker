import unittest
from app import task_tracker

class TestTaskTracker(unittest.TestCase):
    def test_app_runs(self):
        self.assertTrue(task_tracker())

if __name__ == "__main__":
    unittest.main()
