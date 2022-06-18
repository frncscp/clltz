from clltz_v1_main import clltz
import matplotlib.pyplot as plt # for graphing
while True:
    x = input(f'{"*"*14}clltz{"*"*14}\n{"*"*8}github.com/frncscp{"*"*7}\n{"*"*33}\nCollatz Conjecture describes a prediction to any given n natural number following this instructions:\nif its even, n/2;\nif its odd, 3n+1;\nand it will end up in a 4, 2, 1 loop.\n\nMENU:\n1)Basic: executes the conjecture in one number.\n2)Graph: enhancement of basic with graphication of the conjecture.\n3)Infinite: executing the conjecture to consecutive numbers indefinitely.\nType your choice here: ')
    if x == '1':
        x = input('Type any n natural number to proceed with the conjecture: ')
        while x.isnumeric() == False:
                x = input('Wrong data type.\nTry Again: ')
        n = clltz(x)
        n.execute()
        n.results()
    elif x == '2':
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
    elif x == '3':
        x = input('Type any n natural number to proceed with the conjecture: ')
        while x.isnumeric() == False:
            x = input('Wrong data type.\nTry Again: ')
        n = clltz(x)
        while True:
            n.execute()
            n.results()
            n.assign(n.ini+1)
        input('How the fuck did you end up here.\nAnyways,\npress Enter to exit...')
    else:
        break
    choice = input('If you wish to execute a new task, press 1.\nOtherwise, press any key.\nType here: ')
    if choice == '1':
        continue
    else: 
        break