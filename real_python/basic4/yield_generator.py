def yielder():
    n = 1
    print('This is the first call')
    yield n

    n += 1
    print('this is the second call')
    yield n

    n += 2
    print('this is the last call')
    yield n

iterator1 = yielder()
iterator2 = yielder()

next(iterator1)
next(iterator2)
next(iterator2)
next(iterator2)
next(iterator1)