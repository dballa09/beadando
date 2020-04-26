#EX33
e=input("adjon meg egy email cimet: ")
def isValid(e):
    a="*_,?!*:; "
    if "@" not in e:
        return "not valid"
    e=e.split("@")