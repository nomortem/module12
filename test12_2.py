import unittest

# Пример реализации классов Runner и Tournament
class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def run(self, distance):
        return distance / self.speed

    def walk(self, distance):
        return distance / (self.speed / 2)

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            time = runner.run(self.distance)
            results[runner] = time
        # Сортируем результаты по времени и получаем порядок финиша
        results = sorted(results.items(), key=lambda x: x[1])
        return {i + 1: runner.name for i, (runner, _) in enumerate(results)}

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    def test_race_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        self.all_results[1] = tournament.start()
        self.assertTrue(list(self.all_results[1].values())[-1] == "Ник")

    def test_race_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        self.all_results[2] = tournament.start()
        self.assertTrue(list(self.all_results[2].values())[-1] == "Ник")

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        self.all_results[3] = tournament.start()
        self.assertTrue(list(self.all_results[3].values())[-1] == "Ник")


if __name__ == '__main__':
    unittest.main()