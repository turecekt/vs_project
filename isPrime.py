import time

PRINT_TIMINGS = False


def isPrime(n):
    start = time.time()

    def printTime(start):
        if PRINT_TIMINGS:
            print("\rFinished in %f seconds" % (time.time() - start))

    def printProgress(i):
        if PRINT_TIMINGS:
            print("\r%f%%" % (i*i/n*100), end="")

    # Elimitate trivial cases
    if n <= 1:
        printTime(start)
        return False
    if n <= 3:
        printTime(start)
        return True
    if n % 2 == 0 or n % 3 == 0:
        printTime(start)
        return False

    # Use P = 6k +/- 1 to allow iterating by 6
    i = 5
    while i * i <= n:
        printProgress(i)
        if n % i == 0 or n % (i + 2) == 0:
            printTime(start)
            return False
        i += 6

    printTime(start)
    return True
