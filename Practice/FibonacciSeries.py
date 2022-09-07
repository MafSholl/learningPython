
older_fib = 0
old_fib = 1

for n in range(1, 50):
    fib = old_fib + older_fib
    print(older_fib)
    older_fib = old_fib
    old_fib = fib

