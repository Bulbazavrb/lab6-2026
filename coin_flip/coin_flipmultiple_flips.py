from typing import Dict
from .single_flip import flip_coin

def flip_coins(n: int) -> Dict[str, int]:
    """Імітує n підкидань монетки та повертає підраховану кількість."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("Кількість підкидань має бути додатним цілим числом.")

    results = {"орел": 0, "решка": 0}
    for _ in range(n):
        res = flip_coin()
        results[res] += 1
    return results