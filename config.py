from typing import Final
from pymorphy3 import MorphAnalyzer

test_mode: Final[bool] = True  # pass true if you want to switch on test mode
version: Final[str] = "1.1.1"  # version num.

DATABASE_NAME: Final[str] = f"database v{version} {'[test_version]' if test_mode else ''}".strip()
OWNER_ID: Final[int] = 1044385209  # @mazutta (creator's) telegram ID

OP_USERS: Final[list[int]] = [
    OWNER_ID,
]

analyzer: Final[MorphAnalyzer] = MorphAnalyzer(lang="ru")
