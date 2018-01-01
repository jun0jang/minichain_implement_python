from collections import Counter

from fastecdsa.point import Point


def strToPoint(pub_key: str):
    x, y = pub_key.split(",")
    return Point(int(x), int(y))


def check_list_item_duplication(target: list):
    counting = Counter(target).values()
    return not max(counting) > 1
