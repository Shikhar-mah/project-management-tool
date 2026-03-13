from enum import Enum

class Status(str, Enum):
    todo = "TODO"
    in_progress = "IN PROGRESS"
    completed = "COMPLETED"

class Priority(str, Enum):
    low = "LOW"
    medium = "MEDIUM"
    high = "HIGH"

