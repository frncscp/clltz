from clltz_main import clltz
x = input('Type any n natural number to proceed with the conjecture: ')
while x.isnumeric() == False:
    x = input('Wrong data type.\nTry Again: ')
n = clltz(x)
while True:
    n.execute()
    n.results()
    n.assign(n.ini+1)