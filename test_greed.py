def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_fail():
    assert 1 == 1, "1 == 2 failed"

# def rollNew(cls, howMany):
#     import random
#     ret = cls()
#     for int i in range(howMany):
#         ret.dice.append(random.randint(1,6))
#     return ret

if __name__ == "__main__":
    test_sum()
    test_fail()