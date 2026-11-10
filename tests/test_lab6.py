"""
Тести для перевірки функціональності пакета coin_flip та модуля lab6.
"""

import unittest
import sys
import os

# Додаємо папку src до шляху пошуку модулів
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from coin_flip.single_flip import flip_coin
from coin_flip.multiple_flips import flip_coins


class TestCoinFlipPackage(unittest.TestCase):

    def test_single_flip_valid_output(self):
        """Перевірка, що flip_coin повертає 'орел' або 'решка'."""
        result = flip_coin()
        self.assertIn(result, ["орел", "решка"])

    def test_multiple_flips_structure(self):
        """Перевірка структури та суми результатів у flip_coins."""
        n = 50
        results = flip_coins(n)
        self.assertIsInstance(results, dict)
        self.assertIn("орел", results)
        self.assertIn("решка", results)
        self.assertEqual(results["орел"] + results["решка"], n)

    def test_multiple_flips_invalid_input(self):
        """Перевірка реакції на некоректні вхідні дані."""
        with self.assertRaises(ValueError):
            flip_coins(0)
        with self.assertRaises(ValueError):
            flip_coins(-10)
        with self.assertRaises(ValueError):
            flip_coins("10")  # type: ignore


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCoinFlipPackage)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 50)
    print(f"Пройдено тестів: {result.testsRun}")
    print(f"Успішно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Помилок: {len(result.failures) + len(result.errors)}")
    print("=" * 50)

    input("\nНатисніть Enter для виходу...")