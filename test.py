@profile
def test1():
    list1=[i for i in range(100000)]
    list2=[i for i in range(100000)]
    list3=list1+list2
    return

@profile
def test2():
    list1=[i for i in range(100000)]
    list2=[i for i in range(100000)]
    list3=[i for i in range(200000)]

if __name__ == '__main__':
    test1()
    test2()