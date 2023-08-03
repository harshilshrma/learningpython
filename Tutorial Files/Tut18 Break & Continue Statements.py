# i = 0
#
# while True:   # true can also be 1
#     if i+1<5:
#         i = i+1    #to update the value
#         continue
#         #continue ka mtlb to current iteration chal rhi hai usko chalne do(jab tak satisfied
#         #hai condition), aur uske baad ka bbhul jao. jab unsatisfied, tab aage bado!
#     print(i+1, end =" ")
#     if i == 44:
#         i = i+1
#         break
#         #break ka mtlb uss loop ko todd do aur usse bahar nikal jao.
#     i = i+1

###QUIZ
while True:
    inp = int(input("Enter a number:\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100!")
        break
    else:
        print("Try again!\n")
        continue