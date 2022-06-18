from clltz_v1_main import clltz
x = input('Type any n natural number to proceed with the conjecture: ')
while x.isnumeric() == False:
    x = input('Wrong data type.\nTry Again: ')
n = clltz(x)
while True:
    n.execute()
    n.results()
    n.assign(n.ini+1)
input('How the fuck did you end up here.\nAnyways,\npress Enter to exit...')