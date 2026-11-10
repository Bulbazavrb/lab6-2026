"""
Головний модуль лабораторної роботи № 6 (Варіант 12).
Демонстрація використання пакета coin_flip, стандартних бібліотек
та сторонніх пакетів (colorama, tabulate).
"""

import sys
import os
import math
import random
from typing import Dict

# ----------------------------------------------------------------------
# 1. Налаштування шляхів імпорту та завантаження пакета coin_flip
# ----------------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

for path in [current_dir, parent_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

try:
    # Пробуємо імпортувати з пакета coin_flip
    from coin_flip import flip_coin, flip_coins
except ImportError:
    try:
        from src.coin_flip import flip_coin, flip_coins
    except ImportError:
        # Резервний варіант (якщо пакет не знайдено на диску)
        def flip_coin() -> str:
            """Імітує одне підкидання монетки."""
            return random.choice(["орел", "решка"])

        def flip_coins(n: int) -> Dict[str, int]:
            """Імітує n підкидань монетки та повертає результат."""
            if not isinstance(n, int) or n < 1:
                raise ValueError("Кількість підкидань має бути додатним цілим числом.")
            results = {"орел": 0, "решка": 0}
            for _ in range(n):
                results[flip_coin()] += 1
            return results

# ----------------------------------------------------------------------
# 2. Безпечний імпорт сторонніх бібліотек (colorama та tabulate)
# ----------------------------------------------------------------------
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_CYAN = Fore.CYAN + Style.BRIGHT
    COLOR_YELLOW = Fore.YELLOW
    COLOR_GREEN = Fore.GREEN + Style.BRIGHT
    COLOR_RED = Fore.RED
    COLOR_RESET = Style.RESET_ALL
except ImportError:
    # Якщо colorama не встановлено, використовуємо порожні рядки
    COLOR_CYAN = COLOR_YELLOW = COLOR_GREEN = COLOR_RED = COLOR_RESET = ""

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False


# ----------------------------------------------------------------------
# 3. Головна логіка програми
# ----------------------------------------------------------------------
def main():
    print(COLOR_CYAN + "=" * 60)
    print(COLOR_CYAN + "  ЛАБОРАТОРНА РОБОТА № 6: МОДУЛІ ТА ПАКЕТИ (Варіант 12)")
    print(COLOR_CYAN + "=" * 60)

    # --- Одне підкидання монетки ---
    print(COLOR_YELLOW + "\n--- 1. Подиноке підкидання монетки (single_flip) ---" + COLOR_RESET)
    single_res = flip_coin()
    print(f"Результат кидка: {COLOR_GREEN}{single_res.upper()}{COLOR_RESET}")

    # --- Серія підкидань монетки ---
    n_flips = 100
    print(COLOR_YELLOW + f"\n--- 2. Серія з {n_flips} підкидань (multiple_flips) ---" + COLOR_RESET)
    stats = flip_coins(n_flips)

    heads_pct = round((stats['орел'] / n_flips) * 100, 2)
    tails_pct = round((stats['решка'] / n_flips) * 100, 2)

    table_data = [
        ["Орел (Heads)", stats['орел'], f"{heads_pct}%"],
        ["Решка (Tails)", stats['решка'], f"{tails_pct}%"],
        ["Всього (Total)", n_flips, "100.0%"]
    ]
    headers = ["Сторона монети", "Кількість", "Частка"]

    if HAS_TABULATE:
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    else:
        # Резервний вивід, якщо tabulate не встановлено
        print(f"{'Сторона':<15} | {'Кількість':<10} | {'Частка':<10}")
        print("-" * 42)
        for row in table_data:
            print(f"{row[0]:<15} | {row[1]:<10} | {row[2]:<10}")

    # --- Використання стандартного модуля math ---
    print(COLOR_YELLOW + "\n--- 3. Статистичний аналіз за допомогою модуля `math` ---" + COLOR_RESET)
    diff = abs(stats['орел'] - stats['решка'])
    sqrt_diff = round(math.sqrt(diff), 4)
    print(f"Абсолютна різниця між орлами та решками: {diff}")
    print(f"Квадратний корінь відхилення (math.sqrt): {sqrt_diff}")

    print(COLOR_CYAN + "\n[+] Виконання програми завершено успішно." + COLOR_RESET)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(COLOR_RED + f"\n[!] Помилка виконання: {e}" + COLOR_RESET)
    finally:
        # Захист від миттєвого закриття консолі Windows
        input("\nНатисніть Enter для закриття вікна...")