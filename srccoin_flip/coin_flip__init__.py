"""
Пакет coin_flip для імітації підкидання монетки.
Варіант 12.
"""

from .single_flip import flip_coin
from .multiple_flips import flip_coins

__all__ = ["flip_coin", "flip_coins"]