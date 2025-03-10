import random
import sys

LOGGING='off'
NUMBER_OF_ITERATIONS_AT_NO_SOLUTIONS=600000
NUMBER_OF_ITERATIONS_HAS_SOLUTION=100000

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

target_text = str([wanted_result])
input_text = str(numbers)
fill_len = (len(input_text) - len(target_text)) // 2
print('')
print('-----------------------------------------------------------------------'[0:len(input_text)])
print('                            '[0:fill_len] + target_text)
print(input_text)
print('-----------------------------------------------------------------------'[0:len(input_text)])
print("\
\nNotation:\
\n   n : input value\
\n   n_: intermediate result output and end result\
\n  _n : intermediate result input\
\n\
\n   The line starts with a number which is how many calculations has been done so far\
\n   P: [4, 1, 2] | 4 + 1 = 5_ | _5 + 2 = 7_\
\n       meaning: Part using the three input numbers [4, 1, 3] and then this calculation\
\n   Calc Ps: [52, 11] | 52 * 11 = 572_\
\n       meaning: The previously calcated parts are then calculated to the end result\
\n")

logging.out(str(numbers) + '\n')
logging.out(str(wanted_result) + '\n')
logging.out('\n')

# define the function blocks
def addition(origin, x, y):
    return x + y , origin + str(x) + " + " + str(y) + " = " + str(x+y) + '_'

def substraction(origin, x, y):
    if y > x:
        return y-x , str(y) + " - " + origin + str(x) + " = " + str(y-x) + '_'
    return x-y , origin + str(x) + " - " + str(y) + " = " + str(x-y) + '_'

def multiplication(origin, x, y):
    if x == 0 or y == 0 or x == 1 or y == 1:
        return options[random.randint(0,1)](origin, x, y)
    return x * y, origin + str(x) + " * " + str(y) + " = " + str(x*y) + '_'

def division(origin, x, y):
    if x == 0 or y == 0 or x == 1 or y == 1:
        return options[random.randint(0,1)](origin, x, y)
    if (x % y) == 0:
        return x//y, origin + str(x) + " / " + str(y) + " = " + str(x//y) + '_'
    if (y % x) == 0:
        return y//x, str(y) + " / " + origin + str(x) + " = " + str(y//x) + '_'

    return options[random.randint(0,2)](origin, x, y)

# map the inputs to the function blocks
options = {0: addition,
           1: substraction,
           2: multiplication,
           3: division,
           }

log_results = []

def do_math(test_numbers):
    carry = test_numbers.pop(0)
    carry_is_part_result = ''
    if len(test_numbers) == 0:
        # just one number given as input
        log_results.append(str(carry) + ' = ' + str(carry) + '_')
    while len(test_numbers) > 0:
        results = options[random.randint(0,3)](carry_is_part_result, carry, test_numbers.pop(0))
        carry_is_part_result = '_'
        carry = results[0]
        log_results.append(results[1])

    logging.out(' | '.join(log_results) + "  Result: " + str(carry) + "\n")
    return carry

current_result = 0
best_diff = wanted_result
searching = NUMBER_OF_ITERATIONS_AT_NO_SOLUTIONS
best_match = ''
total_calculations = 0
match_length = 1000
while searching > 0:
    del log_results[:]
    total_calculations += 1
    input_numbers = list(numbers)
    random.shuffle(input_numbers)
    start_index = 0
    test_numbers = input_numbers[0:random.randint(1,10)]
    no_of_index = len(test_numbers)
    # log_results.append("Using "+str(test_numbers))
    parantesis_result = []
    while start_index < no_of_index:
        numbers_tot = random.randint(1,no_of_index-start_index)
        curr_list = test_numbers[start_index:start_index+numbers_tot]
        log_results.append('P: '+str(curr_list))
        parantesis_result.append(do_math(curr_list))
        start_index += numbers_tot
    if len(parantesis_result) > 1:
        log_results.append("Calc Ps: " + str(parantesis_result))
        current_result = do_math(parantesis_result)
    else:
        current_result = parantesis_result[0]

    diff = wanted_result - current_result
    if diff < 0:
        diff = -diff
    if diff < best_diff or diff == 0:
        best_diff = diff
        if diff > 0:
            log_results.insert(0, "====> " + str(diff) + " away")
        best_match = ' | '.join(log_results)
        this_len = len(best_match)
        if diff > 0:
            searching = NUMBER_OF_ITERATIONS_AT_NO_SOLUTIONS
        elif this_len < match_length:
            searching = NUMBER_OF_ITERATIONS_HAS_SOLUTION
            print("{:8d} | {}".format(total_calculations, best_match))
            match_length = this_len
            best_match = ''
    else:
        searching -= 1

if best_diff > 0:
    print(best_match)
    print ("Gave up finding any closer solution after", total_calculations, 'calculation')
else:
    print("{:8d} | total calculations".format(total_calculations))

logging.close()
