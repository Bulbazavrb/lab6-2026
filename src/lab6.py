"""
Головний модуль лабораторної роботи № 6.
Демонстрація використання власного пакета coin_flip,
стандартних бібліотек та сторонніх пакетів (colorama, tabulate).
"""

import sys
import os
import math
from colorama import Fore, Style, init
from tabulate import tabulate

# Додаємо шлях до директорії src для коректного імпорту
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from coin_flip import flip_coin, flip_coins

# Ініціалізація colorama для кольорового консольного виводу
init(autoreset=True)


def main():
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + "  ЛАБОРАТОРНА РОБОТА № 6: МОДУЛІ ТА ПАКЕТИ (Варіант 12)")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)

    # 1. Демонстрація single_flip
    print(Fore.YELLOW + "\n--- 1. Подиноке підкидання монетки (single_flip) ---")
    single_res = flip_coin()
    print(f"Результат кидка: {Fore.GREEN + Style.BRIGHT}{single_res.upper()}")

    # 2. Демонстрація multiple_flips
    n_flips = 100
    print(Fore.YELLOW + f"\n--- 2. Серія з {n_flips} підкидань (multiple_flips) ---")
    stats = flip_coins(n_flips)

    # Використання стандартного модуля math для обчислення відсотка
    heads_pct = round((stats['орел'] / n_flips) * 100, 2)
    tails_pct = round((stats['решка'] / n_flips) * 100, 2)

    # Використання стороннього пакета tabulate для гарного виведення
    table_data = [
        ["Орел (Heads)", stats['орел'], f"{heads_pct}%"],
        ["Решка (Tails)", stats['решка'], f"{tails_pct}%"],
        ["Всього (Total)", n_flips, "100.0%"]
    ]
    headers = ["Сторона монети", "Кількість", "Частка"]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    # 3. Використання модуля стандартної бібліотеки math
    print(Fore.YELLOW + "\n--- 3. Статистичний аналіз за допомогою модуля `math` ---")
    diff = abs(stats['орел'] - stats['решка'])
    sqrt_diff = round(math.sqrt(diff), 4)
    print(f"Абсолютна різниця між орлами та решками: {diff}")
    print(f"Квадратний корінь різниці (math.sqrt): {sqrt_diff}")

    print(Fore.CYAN + "\n[+] Демонстраційне виконання завершено успішно.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"\n[!] Помилка виконання: {e}")
    finally:
        input("\nНатисніть Enter для виходу з програми...")