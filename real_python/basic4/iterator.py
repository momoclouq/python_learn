list1 = [1, 2, 3, 4, 5, 6, 7]
iter1 = iter(list1)

while (True):
    try:
        value = next(iter1)
        print(value, end='/')
    except StopIteration:
        break
    finally:
        print('reached finally')

class Test:
    def __init__(self, value):
        self._value = value

    def __iter__(self):
        self._count = self._value
        return self

    def __next__(self):
        if (self._count >= 0):
            self._count -= 1
            return self._count + 1
        else:
            raise StopIteration

list2 = Test(10)

for value in list2:
    print(value)