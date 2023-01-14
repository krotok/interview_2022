def myfunction(n):
    if n == 0:
        return n
    else:
        return myfunction(n - 1)


myfunction(999)  # results in stack overflow error when insert 1000