from dataclasses import dataclass


@dataclass
class Task:
    id: int
    description: str
    is_completed: bool
