import random
import sys

logfile = open('./logfile.txt', 'a+')

numbers = []
if len(sys.argv) == 8:
    for i in range(1, 7):
        numbers.append(int(sys.argv[i]))
    wanted_result = int(sys.argv[7])
else:
    for i in range(0, 6):
        numbers.append(int(input("Enter number: ")))
    wanted_result = int(input("Enter the result: "))

print('Working with', numbers, 'and', wanted_result)

logfile.write(str(numbers) + '\n')
logfile.write(str(wanted_result) + '\n')
logfile.write('\n')

# define the function blocks
def addition(x,y):
    return x + y , str(x) + " + " + str(y) + " = " + str(x+y) + ' | '

def substraction(x,y):
    return x-y , str(x) + " - " + str(y) + " = " + str(x-y) + ' | '

def multiplication(x,y):
    return x * y, str(x) + " * " + str(y) + " = " + str(x*y) + ' | '

def division(x,y):
    if (x % y) == 0:
        return x//y, str(x) + " / " + str(y) + " = " + str(x//y) + ' | '
    else:
        return options[random.randint(0,2)](x, y)

# map the inputs to the function blocks
options = {0: addition,
           1: substraction,
           2: multiplication,
           3: division,
           }

log_results = []

def do_math(numbersinput):
    test_numbers = []
    test_numbers = test_numbers + numbersinput
    random.shuffle(test_numbers)
    del log_results[:]

    while len(test_numbers) > 1:
        results = options[random.randint(0,3)](test_numbers.pop(), test_numbers.pop())
        test_numbers.append(results[0])
        log_results.append(results[1])

    for i in range(0,len(log_results)):
        logfile.write(log_results[i])

    logfile.write("\n" + "Result: " + str(test_numbers[0]) + "\n")
    logfile.write('----------------------\n')
    return test_numbers[0]

current_result = 0
best_diff = -1
searching = 0
while best_diff != 0 and searching < 100000:
    current_result = do_math(numbers)
    diff = wanted_result - current_result
    if diff < 0:
        diff = -diff
    if best_diff < 0 or diff < best_diff:
        best_diff = diff
        for i in range(0,len(log_results)):
            print(log_results[i], end='')
        print("Result: " + str(current_result) + " Diff: ", diff)
        searching = 0
    else:
        searching += 1

if searching > 0:
    print ("Gave up to find any closer solution after", searching, 'iterations')

logfile.close()
