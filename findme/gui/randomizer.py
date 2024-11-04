from dataclasses import dataclass
from pathlib import Path
from secrets import choice
from typing import ClassVar, Self

from findme.utils.basedir import BASE_DIR


@dataclass
class Randomizer:
    """Рандомайзер."""

    _backgrounds_dir: ClassVar[Path] = BASE_DIR / "resources" / "images" / "backgrounds"

    @classmethod
    def get_background(cls: type[Self]) -> Path:
        """Получить путь до случайного заднего фона."""
        return choice([path for path in cls._backgrounds_dir.glob("*") if path.is_file()])