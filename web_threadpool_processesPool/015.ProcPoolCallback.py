import multiprocessing


def function(x):
    return x * x


def use1(pool):
    pool.map_async(function, [1, 2, 3], callback=display)


def use2(pool):
    pool.map_async(function, [3, 4, 5], callback=display)


def use3(pool):
    pool.apply_async(function, [9, ], callback=display)  # it has to be list/tuple even for single argument


def display(result):
    print(result)


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)

    # ... code ...

    use1(pool)

    # ... code ...

    use2(pool)

    # ... code ...

    use3(pool)

    # ... code ...

    pool.close()
    pool.join()
