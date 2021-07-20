from enum import IntEnum


class SubscriptionStatus(IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    CANCELLED = 3


class Package(IntEnum):
    MINI = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    GIANT = 5
    SUPER_GIANT = 6


class Name(IntEnum):
    BALANCED_DIET = 1
    HIGHPROTEIN_DIET = 2
    SENIOR_DOGS = 3
    PUPPY_DOGS = 4


class Delivery(IntEnum):
    DELIVERED = 1
    NOT_DELIVERED = 2
    PENDING = 3
