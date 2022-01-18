import pytest


def check_prime_number(n):
    if n < 2:
        flag = 0
        return False
    for p in range(2, n):
        if n % p == 0:
            return False
    return True


def test(a):
    c = 0
    for i in range(len(a)):
        if check_prime_number(a[i]):
            print('nguyen tố ' + str(i))
            c = c + 1
    if c < 2:
        return False
    else:
        return True


@pytest.mark.parametrize("num,testa",
                         [([12, 24, 36, 28, 10, 14, 16, ], False), ([10, 46, 62, 5, 88], False),
                          ([3, 5, 72, 21, 23, 46, 48], True)])
# Press the green button in the gutter to run the script.
def test_fnc(num, testa):
    assert testa == test(num)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
