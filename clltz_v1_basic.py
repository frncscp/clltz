from clltz_v1_main import clltz
while True:
    x = input(f'{"*"*14}clltz{"*"*14}\n{"*"*8}github.com/frncscp{"*"*7}\n{"*"*33}\nCollatz Conjecture describes a prediction to any given n natural number following this instructions:\nif its even, n/2;\nif its odd, 3n+1;\nand it will end up in a 4, 2, 1 loop.\nType any n natural number to proceed with the conjecture: ')
    while x.isnumeric() == False:
        x = input('Wrong data type.\nTry Again: ')
    n = clltz(x)
    n.execute()
    n.results()
    exit = input('If you wish to run the program again, type 1.\nPress any other key to exit.\nType here: ')
    if exit == '1':
        continue
    else:
        break