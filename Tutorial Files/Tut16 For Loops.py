# list1 = [["Harshil", 12], ["Pewdiepie", 12], ["Mrbeast", 123], ["Ship", 0]]
# # print(list1 [0:3])
#
# dict1 = dict(list1)
# #print(dict1)
#
# for item in list1:
#     print(item)
# for item in dict1:
#     print(item)
# for item, number in dict1.items():
#     print(item, "and number is", number)

###QUIZ
list2 = [int, float, "Harshil", 1, 3, 45, 7, 6, 76]
for items in list2:
    if str(items).isnumeric() and items>=6:                  #str(items) coz int aur float valo ko string bana diya
        print(items)

#for loop jab tak chlta hai, jab tak list etc etc khatam na ho jae jabki while loop tab tak chlta rhega
#jab tak user ki condition satisfy na jaye