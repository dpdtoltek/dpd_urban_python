import rt_with_exceptions as rt_we
import unittest
import logging


class RunnerTest(unittest.TestCase):
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(funcName)s | %(message)s')
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.name = rt_we.Runner('Ben', speed=-5)
            for i in range(10):
                self.name.walk()
            self.assertEqual(self.name.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as verr:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.name = rt_we.Runner(13)
            for i in range(10):
                self.name.run()
            self.assertEqual(self.name.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as terr:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.name1 = rt_we.Runner('Eva')
        self.name2 = rt_we.Runner('Mary')
        for i in range(10):
            self.name1.run()
            self.name2.walk()
        self.assertNotEqual(self.name1.distance, self.name2.distance)


if __name__ == '__main__':
    RunnerTest()
