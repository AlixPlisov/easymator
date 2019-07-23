def x(city, name):
    city = open(city,'r').read()
    city = city.replace('\n', ';')
    city = city.split(';')
    success = []
    for i in city:
        if i:
            success.append(i.lstrip().rstrip())
    success = {k: v for k, v in zip(success[::2], success[1::2])}
    file = open('{0}.txt'.format(name), 'w')
    print(success,file=file)
    file.close()
    res = open('{0}.txt'.format(name), 'r')
    finish = res.read()
    res.close()
    return print(finish)


one = input('Data')
two = input('name city')
x(one, two)
