def fn1():
    value = 1

    def fn2():
        nonlocal value
        value += 1
        return value
    
    return fn2

fn3 = fn1()
print(fn3());
print(fn3());
print(fn3());
print(fn3());

def handleList(item):
    print('well well well, what do we have here', item)
    return item * 2

list = [1, 2, 3, 4, 5, 6, 7, 100]

list = map(handleList, list)

for i in list:
    print(i)