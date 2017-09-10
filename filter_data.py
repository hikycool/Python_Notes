data = [-1, -2 -3, 1, 2, 3]


def fun1(data):
    '''this function for going through all data,
    to get what list we want'''
    unuse_data = []
    for x in data:
        if x < 0:
            unuse_data.append(x)
    for del_num in unuse_data:
        data.remove(del_num)
    print data
    return data


def fun2(data):
    '''this function filter data by filter()'''

    data = filter(lambda x : x>0, data)
    print data
    return data

def fun3(data):
    '''this function by list judgement'''

    data = [x for x in data if x>= 0]
    print data
    return data

def main():
    data1 = fun1(data)
    data2 = fun2(data)
    data3 = fun3(data)

main()
