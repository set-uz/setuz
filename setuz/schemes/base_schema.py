from dataclasses import dataclass
from typing import Optional


@dataclass
class MainSchema:
    count: int
    next: Optional[str]
    prev: Optional[str]
