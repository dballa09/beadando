import numpy as np
#EX1
kor=int(input("adja meg a korok szamat(1-1000): "))
p1=[]
p2=[]
for i in range(kor):
    pont1=int(input("adja meg P1 pontszamat(1-1000): "))
    p1.append(pont1)
    pont2=int(input("adja meg P2 pontszamat(1-1000): "))
    p2.append(pont2)
def biggestLead(kor, p1, p2):
    maxLead=0
    leader=""
    sum1=0
    sum2=0
    for i in range(kor):
        sum1+=p1[i]
        sum2+=p2[i]
        lead=sum1-sum2
        if lead>0:
            if lead>maxLead:
                maxLead=lead
                leader = "P1"
        if lead<0:
            if abs(lead)>maxLead:
                maxLead=abs(lead)
                leader = "P2"
    print(leader, maxLead)
print(biggestLead(kor, p1, p2))







#EX32
# a=["X", "O", "E"]
# amoba=np.random.choice(a, (3, 3))
# def winner(amoba):
#     if amoba[0,0] and amoba[0,1] and amoba[0,2]:
#         return "X"
#     else:
#         return "egyenlo"
# print(amoba)
# print(winner(amoba))
#
#
#
#
#
# #EX33
# e=input("adjon meg egy email cimet: ")
# def isValid(e):
#     a=" _,?!*:;"
#     d = [".com", ".hu"]
#     if "@" not in e:
#         return "not valid"
#     e=e.split("@")
#     for ch1 in e[0]:
#         if ch1 in a:
#             return "not valid"
#         else:
#             for ch2 in e[1]:
#                 l=len(e[1])
#                 if ch2[0].isupper()==True:
#                     return "not valid"
#                 if ch2 in a:
#                     return "not valid"
#                 if e[1][l-3:l] not in d:
#                     return "not valid"
#     return "valid"
#
# print(isValid(e))