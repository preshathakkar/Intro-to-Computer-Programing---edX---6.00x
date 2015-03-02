def probTest(limit):
    n = 1
    notOne = 5.0/6.0
    One = 1.0/6.0
    prob = 1.0/6.0
    while limit < prob:
        n += 1
        prob = (One)*((notOne)**(n-1))
    return n

def probTest1(limit):
    notOne = 5.0/6.0
    one = 1.0/6.0
    count = 1
    prob = one
    while prob > limit:
        prob=prob*notOne
        count+=1
    #print str('Rolls: ' + str(count))
    #print str(prob)
    return count

def probTest2(limit):
    n = 1
    notOne = 5.0/6.0
    One = 1.0/6.0
    prob = (One)*((notOne)**(n-1))
    while prob > limit:
        prob = (One)*((notOne)**(n-1))
        n += 1
    print n    
    return n

def probTest3(limit):
    n = 1
    notOne = 5.0/6.0
    One = 1.0/6.0
    prob = One
    while prob>limit:
        n=n+1
        prob=prob*notOne
        if prob == limit:
            return n
        
    return n


def probTest4(limit):
    if limit <= 0 or limit >= 1.0/6:
        return 0
    n = 0
    p = 1.0/6
    while p > limit:
        n += 1
        p = (1.0/6)*((5.0/6)**(n))
    return n




def probTest5(limit):
    if limit <= 0 or limit > 1.0/6:
        return 0
    n = 1
    p = 1.0/6

    while p > limit:
        n += 1
        p = (1.0/6)*((5.0/6)**(n-1))

    return n
