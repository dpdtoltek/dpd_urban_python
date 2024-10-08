import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        all_res = [cls.all_results.get(result) for result in cls.all_results]
        for i in all_res:
            for key, value in i.items():
                i[key] = value.name
            print(i)

    def test_start1(self):
        self.tournament1 = rat.Tournament(90, self.runner1, self.runner3)
        result1 = self.tournament1.start()
        TournamentTest.all_results['test_start1'] = result1
        last = result1[max(result1)]
        self.assertTrue(last == 'Ник')

    def test_start2(self):
        self.tournament2 = rat.Tournament(90, self.runner2, self.runner3)
        result2 = self.tournament2.start()
        TournamentTest.all_results['test_start2'] = result2
        last = result2[max(result2)]
        self.assertTrue(last == 'Ник')

    def test_start3(self):
        self.tournament3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = self.tournament3.start()
        TournamentTest.all_results['test_start3'] = result3
        last = result3[max(result3)]
        self.assertTrue(last == 'Ник')

    def test_start4(self):
        self.tournament4 = rat.Tournament(6,  self.runner3, self.runner2, self.runner1)
        result4 = self.tournament4.start()
        TournamentTest.all_results['test_start4'] = result4
        last = result4[max(result4)]
        self.assertTrue(last == 'Ник', 'Последний не Ник.')

    def test_start5(self):
        self.tournament5 = rat.Tournament(18,  self.runner2, self.runner1)
        result5 = self.tournament5.start()
        TournamentTest.all_results['test_start5'] = result5
        last = result5[max(result5)]
        self.assertTrue(last == 'Андрей', 'Последний не Андрей.')


if __name__ == '__main__':
    TournamentTest()
