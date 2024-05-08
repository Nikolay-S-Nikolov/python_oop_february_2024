
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_is_initialized_correctly(self):
        # Act
        worker = Worker("Test", 1000, 60)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)

    def test_energy_incremented_after_rest(self):
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)

        worker.rest()
        self.assertEqual(61, worker.energy)

        worker.rest()
        self.assertEqual(62, worker.energy)

    def test_worker_work_with_negative_or_0_energy_error_raised(self):
        worker = Worker("Test", 1000, 1)
        self.assertEqual(1, worker.energy)
        worker.work()
        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

        worker_1 = Worker("Test", 1000, -1)
        with self.assertRaises(Exception) as ex:
            worker_1.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increased_by_salary_after_work(self):
        worker = Worker("Test", 1000, 60)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(1000, worker.money)

    def test_worker_energy_decreased_after_work(self):
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)
        worker.work()
        self.assertEqual(59, worker.energy)

    def test_get_info_method_returns_proper_string_and_values(self):
        # Arrange
        worker = Worker("Test", 1000, 60)
        # Act
        result = worker.get_info()
        # Assert
        self.assertEqual('Test has saved 0 money.', result)

        worker.work()
        result = worker.get_info()
        self.assertEqual('Test has saved 1000 money.', result)


if __name__ == '__main__':
    main()
