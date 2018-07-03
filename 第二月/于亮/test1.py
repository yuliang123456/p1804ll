'''
def hs(d):
    t=open('d','a+')
    b=t.read()
    t=open('d','w')
    if len(b) == 0:
        print('hahaha')
        t.write('hahaha')
    else:
        print(b)
    t.close()
hs('d')
'''

import os
'''
def shanchu(tt):
    os.remove(tt)

shanchu('1.py')
'''


def genggai(tt1,tt2):

    os.rename(tt1,tt2)
genggai('2.py','3.py')


