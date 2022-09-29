# import sys
from datetime import datetime
from collections import defaultdict
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) != 2:
    print(bcolors.FAIL + 'Incorrect number of arguments. Please specify a file.')
    sys.exit(0)

filename = sys.argv[1]

def stringifyEntries(entries):
    if len(entries) == 0:
        return ""
    entries_string = ""
    for key, value in entries.items():
        valuestr = ". ".join(value)
        entries_string += "["+key+"]"+" - "+valuestr+"\n" 
    return entries_string

entries = defaultdict(list)

while True:
    print('\033[2J')
    print('\033[H')
    print(bcolors.OKBLUE + 'Writing to \'' + filename + '\'' + bcolors.ENDC)
    user_input = input(stringifyEntries(entries))
    if user_input == "quit":
        break
    current_time = datetime.now().strftime("%H:%M")
    entries[current_time].append(user_input)  
    file = open(filename, "w")
    file.write(stringifyEntries(entries))
    file.close()



