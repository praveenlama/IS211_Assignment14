#Praveen Lama


def fibonacci(n):
    if n <= 1: # exit condition
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a,b):
    while b:
        (a,b) = (b, (a%b))
    return a


def compareTo(s1, s2):
    ts1 = s1[0:1]
    ts2 = s2[0:1]

    if len(s1) == 0 and len(s2) == 0: # matched / end of comparison
        return 0
    elif len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1

    if ord(ts1)<ord(ts2):
        return -1
    elif ord(ts1)>ord(ts2):
        return 1

    return compareTo(s1[1:], s2[1:]) # for next

if __name__ == "__main__":
    print 'Testing fibonacci() Function'
    print fibonacci(5)
    print fibonacci(20)

    print '\nTesting gcd() Function'
    print gcd(27,3)
    print gcd(8, 2)
    print gcd(19, 2)
    print gcd(45, 15)

    print '\nTesting compareTo() Function'
    print compareTo("class","classes")
    print compareTo("classes", "class")
    print compareTo("glass", "class")
    print compareTo("class","class")