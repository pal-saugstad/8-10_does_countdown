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

print("Notation:")
print("   n : input value")
print("   n_: intermediate result output and end result")
print("  _n : intermediate result input")

target_text = str([wanted_result])
input_text = str(numbers)
fill_len = (len(input_text) - len(target_text)) // 2
print('')
print('-----------------------------------------------------------------------'[0:len(input_text)])
print('                            '[0:fill_len] + target_text)
print(input_text)
print('-----------------------------------------------------------------------'[0:len(input_text)])
print('')

logging.out(str(numbers) + '\n')
logging.out(str(wanted_result) + '\n')
logging.out('\n')

# define the function blocks
def addition(origin, x, y):
    return x + y , origin + str(x) + " + " + str(y) + " = " + str(x+y) + '_'

def substraction(origin, x, y):
    return x-y , origin + str(x) + " - " + str(y) + " = " + str(x-y) + '_'

def multiplication(origin, x, y):
    return x * y, origin + str(x) + " * " + str(y) + " = " + str(x*y) + '_'

def division(origin, x, y):
    if (x % y) == 0:
        return x//y, origin + str(x) + " / " + str(y) + " = " + str(x//y) + '_'
    else:
        return options[random.randint(0,2)](origin, x, y)

# map the inputs to the function blocks
options = {0: addition,
           1: substraction,
           2: multiplication,
           3: division,
           }

log_results = []

def do_math(numbersinput):
    test_numbers = list(numbersinput)
    random.shuffle(test_numbers)
    del log_results[:]
    carry = test_numbers.pop()
    carry_is_part_result = ''
    while len(test_numbers) > 0:
        results = options[random.randint(0,3)](carry_is_part_result, carry, test_numbers.pop())
        carry_is_part_result = '_'
        carry = results[0]
        log_results.append(results[1])

    for i in range(0,len(log_results)):
        logging.out(log_results[i])

    logging.out("\n" + "Result: " + str(carry) + "\n")
    logging.out('----------------------\n')
    return carry

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
        print(' | '.join(log_results)  + " | Diff: " + str(diff))
        searching = 0
    else:
        searching += 1

if searching > 0:
    print ("Gave up to find any closer solution after", searching, 'iterations')

logging.close()
