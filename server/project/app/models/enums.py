from enum import IntEnum, StrEnum, auto


class NoteColor(IntEnum):
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4


class NoteCategory(StrEnum):
    SOCIAL = auto()
    PHYSICAL = auto()
    SPIRITUAL = auto()
    PSYCHOLOGICAL = auto()
