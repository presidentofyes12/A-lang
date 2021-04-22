eqtypes = ["+", "-", "/", "*"]
def isequation(tocheck):
    global eqtypes
    if eqtypes[0] in tocheck:
        return True
    elif eqtypes[1] in tocheck:
        return True
    elif eqtypes[2] in tocheck:
        return True
    elif eqtypes[3] in tocheck:
        return True
    else:
        return False
