################
## The Parser ##
################
def throw(reason):
    print("Error: " + reason)
vardict = {}
varnames = []
commandnames = ["write", "use", "execute", "getinput", "var"]
def parser(code):
    global varnames
    global vardict
    thing1 = code.split("\"")
    thing2 = code.split("'")
    code = code.split(" ")
    first = code[0]
    if len(code) > 1:
        second = code[1]
    fullstatement = ""
    if first == "write":
        if len(code) > 2:
            if code[1] == "statement":
                try:
                    print(thing1[1])
                except:
                    throw("No quotations")
            elif code[1] == "file":
                try:
                    with open(code[2], 'r') as fin:
                        print(fin.read())
                except FileNotFoundError:
                    throw("File " + code[2] + " doesn't exist")
            elif code[1] == "variable":
                if code[2] in varnames:
                    print(vardict[code[2]])
                else:
                    throw("The variable " + code[2] + " doesn't exist")
            elif code[1] == "getinput":
                print(input())
            elif code[1] == "equation":
                print(eval(thing1[1]))
            else:
                throw(second + " not a valid output type")
        elif len(code) < 2:
            throw(code + " not a valid statement- did you mean 'write statement'?")
        else:
            throw(code + " not a valid statement- must add a string to output")
    elif first == "use":
        try:
            with open(code[1] + ".a", 'r') as fin:
                fullfile = fin.read().split("\n")
                for i in range(0, len(fullfile)):
                    parser(fullfile[i])
                # parser(fin.read())
        except FileNotFoundError:
            throw(code[1] + " doesn't exist")
    elif first == "getinput":
        x = input()
    elif first == "var":
        if code[2] == "=":
            if code[3] == "getinput":
                x = input()
                vardict.update({code[1]: x})
                varnames.append(code[1])
            else:
                vardict.update({code[1]: code[3]})
                varnames.append(code[1])
        else:
            pass # will throw error
    elif len(code) == 1 and first in varnames:
        print(first)
    else:
        pass
def commentornot(statement, execution1, execution2):
    statement = statement.split(" ")
##################
## The Compiler ##
##################
print("Welcome to the A compiler.")
while True:
    try:
        myline = input(">> ")
        if len(myline) < 1:
           continue
        if myline != "end":
            if myline.split()[0] in commandnames:
                parser(myline)
                continue
            elif myline == "quit":
                print("Use 'end' to quit the interpreter")
            elif myline in varnames:
                print(vardict[myline])
            else:
                if myline.split()[0] == "//":
                    continue
                else: throw(myline + " not a valid statement")
        elif myline == "end":
            break
        else:
            throw(myline + " not a valid statement")
    except KeyboardInterrupt:
        print("would you like to quit?")
        yesorno = input(">")
        if yesorno == "y":
            break
        elif yesorno == "n":
            print("Ok.")
            continue
