list_card = ['lisi',45,'nan']
a = 100
def test1():
    global a
    a = a + 1
    print(a)
    list_card[2] = 'nv'
    list_card.append('001')
    print(list_card)
def test2():
    print(a)

test1()
test2()
