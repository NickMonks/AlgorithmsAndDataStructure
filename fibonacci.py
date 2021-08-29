def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

def getNthFib(n, memoize = {2: 1, 1:0}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]

def getNthFib(n):
        
    # initialise base case
    lastTwo = [0,1]
    counter = 3 
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1 # warning, doing this we will have counter = n+1, so we need to substract 1
        
    # an edge cas emight be if we want to return fib(1), in that case we return the first value which is
    # our case is lastTwo[0]
    return lastTwo[1] if n > 1 else lastTwo[0]

