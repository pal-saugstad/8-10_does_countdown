import random
import sys

LOGGING='off'


class Logging:
    def __init__(self, active):
        self.active = active
        self.file = ''
        if active:
            self.file = open('./logfile.txt', 'a+')
    def out(self, text):
        if self.active:
            self.file.write(text)
    def close(self):
        if self.active:
            self.file.close()


logging = Logging(LOGGING == 'on')

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

logging.out(str(numbers) + '\n')
logging.out(str(wanted_result) + '\n')
logging.out('\n')

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

def do_math(wanted_result, numbersinput):
    test_numbers = list(numbersinput)
    random.shuffle(test_numbers)
    del log_results[:]
    found_res = []
    carry = test_numbers.pop()
    best_diff = wanted_result - carry
    if best_diff < 0:
        best_diff = -best_diff
    while len(test_numbers) > 0 and carry != wanted_result:
        results = options[random.randint(0,3)](carry, test_numbers.pop())
        carry = results[0]
        diff = carry - wanted_result
        if diff < 0:
            diff = -diff
        log_results.append(results[1])
        found_res.append([carry, diff])
        if diff < best_diff:
            best_diff = diff

    logging.out("Part equations: " + str(log_results) + "\n")
    logging.out("Part res: " + str(found_res) + "\n")
    carry, this_part_diff = found_res.pop()
    while this_part_diff != best_diff and len(found_res) > 0:
        log_results.pop()
        carry, this_part_diff = found_res.pop()

    for i in range(0,len(log_results)):
        logging.out(log_results[i])

    logging.out("\n" + "Result: " + str(carry) + "\n")
    logging.out('----------------------\n')
    return carry

current_result = 0
best_diff = -1
searching = 0
while best_diff != 0 and searching < 100000:
    current_result = do_math(wanted_result, numbers)
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

logging.close()
