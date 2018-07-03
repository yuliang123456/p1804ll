def counter(start=0):
    def incr():
        nonlocal start
        start +=1
        print (start)
        return 'zidingyi'
    return incr
c1=counter(1)
print(c1())
c1()
c1()
c1()
b1=counter(2)
b1()
