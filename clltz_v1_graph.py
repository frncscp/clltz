from clltz_v1_main import clltz
import matplotlib.pyplot as plt
while True:
    print(f'{"*"*11}clltz_graph{"*"*11}\n{"*"*8}github.com/frncscp{"*"*7}\n{"*"*33}\nCollatz Conjecture describes a prediction to any given n natural number following this instructions:\nif its even, n/2;\nif its odd, 3n+1;\nand it will end up in a 4, 2, 1 loop.\n\nThis program will graph:\n1)Iterations\n2)Times that n/2 formula was used\n3)Times that 3n+1 formula was used\n')


    sfs = { #this dictionary will be useful to iterate and know which values are actually numeric
        'start' : input('¿From which natural positive number you want to start?: '),
        'finish' : input('¿To what number you want to get?: '),
        'step' : input('Type step: ')
    } 

    for label, value in sfs.items(): #looping through the dict
        while sfs[label].isnumeric() == False:
            sfs[label] = input(f'Wrong data type on {label} variable\nTry Again: ')

    #assigning actual variables
    start = int(sfs['start'])
    finish = int(sfs['finish'])
    step = int(sfs['step'])

    if finish < start: #it interchanges values if finish is less than start
        finish, start = start, finish
    print('\n')
    numbers = [start] #number array that will be x axis, it begin with the start value
    iterations = []
    mul = []
    div = []
    n = clltz(69) #any number is fine, it'll be asigned later
    for i in range (start, finish+1, step): #1st value = start, last value = finish, step = step
        while numbers[-1] < finish: 
            print(f'Loading set of numbers: {round(len(numbers)/finish*100*step,2)}%', end = '\r')
            #while the -1 number is less than the final one, add a new value that is the sum of the last and the step
            numbers.append(numbers[-1]+step)
        if numbers[-1] > finish: #checking if the last value is greater than the finish one
            numbers.remove(numbers[-1])
    print('\nDone\n')
    i = 0
    for number in numbers: #iterating through the list, execute the collatz conjecture to each number
        print(f'Executting and plotting graph: {round(i/len(numbers)*100, 2)}%', end = '\r')
        n.assign(number) #assign number from the list for the clltz class variable
        n.execute() #execute the conjecture
        #save the results of each iteration for graphing later
        iterations.append(n.itrs)
        mul.append(n.mul)
        div.append(n.div)
        i +=1
    print('\nDone\n')

    title = f'Collatz Conjecture in ({start}, {finish}]'
    if step > 1:
        title += (f'\nUsing a skip counting of {step}')
    plt.title(title)
    plt.plot(numbers, iterations, color = 'blue') #iterations graph
    plt.plot(numbers, div, color = 'purple') #divisions graph
    plt.plot(numbers, mul, color = 'cyan') #multiplications graph
    plt.legend(['Iterations', 'n/2', '3n+1'])
    plt.show()
    exit = input('If you wish to run the program again, type 1.\nPress any other key to exit.\nType here: ')
    if exit == '1':
        continue
    else:
        break