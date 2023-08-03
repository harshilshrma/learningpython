# l = 10  #global
#
# def function1(n):
#     m = 8 #local    # function sabse pehle local ko check krega, fir global ko
#     # l = 5 #local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(l)

x= 89
def harry():
    x = 22
    def john():
        global x
        x = 88
    # print("before calling john()", x)
    john()
    print("after calling john()", x)

harry()
print(x)


