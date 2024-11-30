import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def walk(self, distance):
        self.distance += distance * self.speed

    def run(self, distance):
        self.distance += distance * self.speed


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        remaining_distance = self.distance
        step = 1
        place = 1
        while remaining_distance > 0:
          for runner in self.runners:
            if remaining_distance <= 0:
              break
            run_distance = min(remaining_distance, step)
            runner.run(run_distance)
            remaining_distance -= run_distance
          place +=1

        sorted_runners = sorted(self.runners, key=lambda x: x.distance, reverse=True)
        for i, runner in enumerate(sorted_runners):
            results[i+1] = runner.name
        return results

class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, result in enumerate(cls.all_results.values()):
            print(result)

    def test_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        self.all_results[1] = tournament.start()
        self.assertEqual(list(self.all_results[1].values())[-1], "Ник")

    def test_andrei_nick(self):
        tournament = Tournament(90, [self.andrei, self.nick])
        self.all_results[2] = tournament.start()
        self.assertEqual(list(self.all_results[2].values())[-1], "Ник")

    def test_usain_andrei_nick(self):
        tournament = Tournament(90, [self.usain, self.andrei, self.nick])
        self.all_results[3] = tournament.start()
        self.assertEqual(list(self.all_results[3].values())[-1], "Ник")


if __name__ == '__main__':
    unittest.main()
