def fibonaci (n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonaci (n-1) + fibonaci (n-2)
print(fibonaci(3)) 