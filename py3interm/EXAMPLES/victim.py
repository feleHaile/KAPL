#!/usr/bin/python3

for file in sys.argv[:-1]:
    print("Processing",file)
    f = open(file,"r")
    for line in file:
        count = count + 1
        print(line)
