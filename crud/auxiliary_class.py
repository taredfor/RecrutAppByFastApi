from enum import Enum


class Roles(Enum):
    SITH = "SITH"
    RECRUT = "RECRUT"
    ADMIN = "ADMIN"


class Planets(Enum):
    JUPITER = "JUPITER"
    MARS = "MARS"


class HireTypes(Enum):
    WAITING = "WAITING"
    HIRED = "HIRED"
    NOT_HIRED = "NOT_HIRED"
    NOT_RECRUT = "NOT_RECRUT"