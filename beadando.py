#EX33
e=input("adjon meg egy email cimet: ")
def isValid(e):
    a=" _,?!*:;"
    d = [".com", ".hu"]
    if "@" not in e:
        return "not valid"
    e=e.split("@")
    for ch1 in e[0]:
        if ch1 in a:
            return "not valid"
        else:
            for ch2 in e[1]:
                l=len(e[1])
                if ch2[0].isupper()==True:
                    return "not valid"
                if ch2 in a:
                    return "not valid"
                if e[1][l-3:l] not in d:
                    return "not valid"
    return "valid"

print(isValid(e))