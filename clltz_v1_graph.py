from clltz_main import clltz
import matplotlib.pyplot as plt

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

numbers = [start] #number array that will be x axis, it begin with the start value
iterations = []
mul = []
div = []
n = clltz(69) #any number is fine, it'll be asigned later

for i in range (start, finish+1, step): #1st value = start, last value = finish, step = step
    while numbers[-1] < finish: 
        #while the -1 number is less than the final one, add a new value that is the sum of the last and the step
        numbers.append(numbers[-1]+step)
    if numbers[-1] > finish: #checking if the last value is greater than the finish one
        numbers.remove(numbers[-1])

for number in numbers: #iterating through the list, execute the collatz conjecture to each number
    n.assign(number) #assign number from the list for the clltz class variable
    n.execute() #execute the conjecture
    #save the results of each iteration for graphing later
    iterations.append(n.itrs)
    mul.append(n.mul)
    div.append(n.div)

plt.title(f'Collatz Conjecture in ({start}, {finish}]')
plt.plot(numbers, iterations, color = 'blue') #iterations graph
plt.plot(numbers, div, color = 'purple') #divisions graph
plt.plot(numbers, mul, color = 'cyan') #multiplications graph
plt.legend(['Iterations', 'Multiplications', 'Divisions'])
plt.show()