from enum import Enum


class Map(Enum):
    NONE = 0,
    BIND = 1,
    HAVEN = 2,
    SPLIT = 3,
    ASCENT = 4,
    ICEBOX = 5,
    BREEZE = 6,
    FRACTURE = 7,
    PEARL = 8,
    LOTUS = 9,
    SUNSET = 10


class Region(Enum):
    NONE = 0,
    NA = 1,
    EMEA = 2,
    APAC = 3,
    CN = 4,


class MatchVsNote(Enum):
    BO1 = 1,
    BO3 = 3,
    BO5 = 5


class TieBreaker(Enum):
    MATCH_DIFF = 1
    MAP_DIFF = 2
    ROUND_DIFF = 3


class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETE = 2
