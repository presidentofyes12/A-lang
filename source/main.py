################
##   Notes    ##
################
"""
TODO:
1. Convert importedlibraries to a variable and create an "as" system in the "use" command. [done]
2. Solve this problem: []
var boi = 3
use boitest
(in boitest
var boi = 4
)
what would boi be? 3 or 4?
solve this by using this:
boitest.boi = 4
and only if specifically mentioned to let boitest.boi override infile boi, like this:
use all from boitest
could boi = 4
3. Equations [done]
4. vectors? []
"""
################
## The Parser ##
################
import os.path
from isequation import *
def throw(reason):
    print("Error: " + reason)
vardict = {}
varnames = []
commandnames = ["write", "use", "execute", "getinput", "var", "func"]
importedlibraries = {}
libnames = []
def parser(code):
    global varnames
    global vardict
    global importedlibraries
    strcode = code
    thing1 = code.split("\"")
    vareq = code.split("=")
    """funccommand = None
    isfunction = False
    try:
        thing2 = code.split("()")
        funccommand = thing2[0]
        isfunction = True
        outfile = False
        try:
            funccommand = funccommand.split(".")
            print(funccommand)
            outfile = True
        except:
            outfile = False
        return ""
    except:
        isfunction = False"""
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
        if os.path.exists(code[1].split(".")[0]+".a"):
            if len(code) == 4:
                with open(code[1] + ".a", 'r') as fin:
                    fullfile = fin.read().split("\n")
                    for i in range(0, len(fullfile)):
                        parser(fullfile[i])
                    importedlibraries.update({code[1]: code[3]})
                    libnames.append(code[1])
            elif len(code) == 2:
                with open(code[1] + ".a", 'r') as fin:
                    fullfile = fin.read().split("\n")
                    for i in range(0, len(fullfile)):
                        parser(fullfile[i])
                    importedlibraries.update({code[1]: code[1]})
                    libnames.append(code[1])
            else:
                throw(code[1] + " doesn't exist")
        elif os.path.exists(code[1].split(".")[0]+".py"):
            if len(code) == 4:
                with open(code[1] + ".py", 'r') as fin:
                    fullfile = fin.read().split("\n")
                    for i in range(0, len(fullfile)):
                        exec(fullfile[i]) # or exec()
                    importedlibraries.update({code[1]: code[3]})
                    libnames.append(code[1])
            elif len(code) == 2:
                with open(code[1] + ".py", 'r') as fin:
                    fullfile = fin.read().split("\n")
                    for i in range(0, len(fullfile)):
                        exec(fullfile[i]) # or exec()
                    importedlibraries.update({code[1]: code[1]})
                    libnames.append(code[1])
        else:
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
                if "\"" in code[3]:
                    vardict.update({code[1]: thing1[1]})
                    varnames.append(code[1])
                else:
                    if code[3] in varnames:
                        othervarval = vardict[code[3]]
                        vardict.update({code[1]: othervarval})# assigns var value to new var
                        varnames.append(code[1])
                    else:
                        try:
                            vardict.update({code[1]: int(vareq[1])}) # or int(code[3])
                            varnames.append(code[1])# is int?
                        except:
                            try:
                                vardict.update({code[1]: float(vareq[1])})
                                varnames.append(code[1])# is float?
                            except:
                                if isequation(vareq[1]):
                                    vardict.update({code[1]: eval(vareq[1])})
                                    varnames.append(code[1])# is equation?
                                else:
                                    throw(code[3] + " isn't a variable")
        else:
            pass # will throw error
    elif first == "func":
        pass
    elif len(code) == 1 and first in varnames:
        print(vardict[first])
    elif isequation(strcode):
        print(eval(strcode))
    else:
        pass

"""elif isfunction:
    if outfile:
        # 1: remove the dot
        # 2: run it again
        funccommand.pop(0)
        # parser(funccommand[0])
        print(funccomand[0])
        pass
    else:
        # this is where step 2 of ^^ comes in
        print(funccommand)"""
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
        if myline != "quit":
            if myline.split()[0] in commandnames:
                parser(myline)
                continue
            elif myline == "end":
                print("Use 'quit' to quit the interpreter")
            elif myline in varnames:
                print(vardict[myline])
            else:
                if myline.split()[0] == "//":
                    continue
                elif isequation(myline):
                    parser(myline)
                else: throw(myline + " not a valid statement")
        elif myline == "quit":
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
