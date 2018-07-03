


def wai(a,b):
    def nei(x):

        print('y=%d*%d+%d'%(a,x,b))
        y = a*x+b
        return y

    return nei
w = wai(2,3)
print(w(3))
