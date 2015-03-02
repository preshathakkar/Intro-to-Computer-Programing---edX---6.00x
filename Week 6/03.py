def isPrime(n):
    try:    
        if n == 1:
            result = False
        else:
            for x in range(2,n):
                if n%x == 0:
                    result = False
            result = True
    except TypeError:
        print "This isn't an integer"
    except ValueError:
        print "The number is not a positive integer"
    else:
        return result
    
import math
def isPrime3(n):
    try:
        if n <= 2:
            return True
        if n % 2 == 0:
            return False

        cntr = 3 # The first odd divisor is 2.
        stopPoint = math.sqrt(n)
        while cntr <= stopPoint:
            if n % cntr == 0: return False
            cntr += 2
        return True
    except TypeError:
        raise TypeError("abc")
    except ValueError:
        raise ValueError("xyz")
    
