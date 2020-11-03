################
## The Parser ##
################
def throw(reason):
    print("Error: " + reason)
def parser(code):
    code = code.split()
    first = code[0]
    fullstatement = ""
    for i in code:
        print
    if first == "write":
        if len(code) > 2:
            if code[1] == "statement":
                print(code[2])
            elif code[1] == "file":
                with open(code[2], 'r') as fin:
                    print(fin.read())
            else:
                throw(second + " not a valid output type")
        elif len(code) < 2:
            throw(code + " not a valid statement- did you mean 'write statement'?")
        else:
            throw(code + " not a valid statement- must add a string to output")
    elif first == "use":
        try:
            with open(code[1] + ".a", 'r') as fin:
                parser(fin.read())
        except FileNotFoundError:
            throw(code[1] + " doesn't exist")
    elif first == "getinput":
        x = input()
        print(x)
def commentornot(statement, execution1, execution2):
    statement = statement.split()
##################
## The Compiler ##
##################
print("Welcome to the A compiler.")
while True:
    myline = input(">> ")
    if len(myline) < 1:
       continue
    if myline != "end":
        if "write" in myline or "execute" in myline or "use" in myline or "getinput" in myline:
            parser(myline)
            continue
        elif myline == "quit":
            print("Use 'end' to quit the interpreter")
        else:
            if myline.split()[0] == "//":
                continue
            else: throw(myline + " not a valid statement")
    elif myline == "end":
        break
    else:
        throw(myline + " not a valid statement")
