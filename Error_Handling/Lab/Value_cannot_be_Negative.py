class ValueCannotBeNegative(Exception):
    """Value cannot be negative"""
    pass


for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
