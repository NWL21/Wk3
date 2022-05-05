import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [1, 2, 3, 64, 34, 25, 12, 22, 11, 90]
    test_arr = [1, 2, 3, 11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [1, 2, 3, 64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11, 3, 2, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [1, 2, 3, 64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_over10num():
    result = [-1, -1]
    input_arr = [1, 2, 3, 64, 34, 25, 12, 22, 11, 90, 4]
    for i in range(1, 3):
        result[i - 1] = Lab3.bubble_sort(input_arr, i)

    assert (result[0] | result[1] == 1)

def test_bubble_sort_under10num():
    result = [-1, -1]
    input_arr = [1, 2, 3, 64, 34, 25, 12, 22, 11]
    for i in range(1, 3):
        result[i - 1] = Lab3.bubble_sort(input_arr, i)

    assert (result[0] | result[1] == 2)

def test_bubble_sort_nonum():
    result = [-1, -1]
    input_arr = []
    for i in range(1, 3):
        result[i - 1] = Lab3.bubble_sort(input_arr, i)

    assert (result[0] | result[1] == 0)

def test_bubble_sort_nonint():
    result = [-1, -1, -1]
    tresult = 0
    change = ['a', "abc", True]
    input_arr = [1.12345, 2, 3, 64, 34, 25, 12, 22, 11, 90]
    for i in range(3):
        input_arr[0] = change[i]
        result[i] = Lab3.bubble_sort(input_arr, 1)
    for i in result:
        tresult = tresult | i

    assert (tresult == 3)