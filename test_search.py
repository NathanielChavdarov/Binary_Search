import search as s
import random

search_list = ["apple", "pear", "lemon", "lime", "melon", "banana"]

def test_emptylist():
    result = s.search([], "tree")
    assert result == -1


def test_listlen1_present():
    result = s.search([9], 9)
    assert result == 0


def test_listlen1_notpresent():
    result = s.search([7], 1)
    assert result == -1


def test_longlist():
    result = s.search([7, 12, 5, 4, 6, 7], 4)
    assert result == 3


def test_superlonglist():
    longlist = [
        random.randint(0, 789123789123789) for i in range(1000000)
    ]
    j = longlist[750000]
    print("starting search")
    result = s.search(longlist, j)
    assert result == 750000
