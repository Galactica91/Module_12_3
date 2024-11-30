import unittest
from unittest import skip
import runner_test
import tournament_test

def freeze_check(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_check
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @freeze_check
    def test_walk(self):
        self.assertTrue("runner" in "runner test")

    @freeze_check
    def test_challenge(self):
        self.assertFalse(5 > 10)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_check
    def test_first_tournament(self):
        self.assertEqual("tournament", "tournament")

    @freeze_check
    def test_second_tournament(self):
        self.assertGreater(10, 5)

    @freeze_check
    def test_third_tournament(self):
        self.assertIn(3, [1, 2, 3])

# Запуск TestSuite
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
    unittest.TextTestRunner().run(suite)