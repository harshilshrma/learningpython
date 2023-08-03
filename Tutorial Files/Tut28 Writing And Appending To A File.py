# f = open("harshil.txt", "w")
# a = f.write("Harshil bhot accha hai\n")
# print(a)
# f.close()

# f = open("harshil2.txt", "a")
# a = f.write("Harshil bhot accha hai\n")
# print(a)
# f.close()

#Handle read and write both
f = open("harshil2.txt", "r+")
print(f.read())
f.write("thank you")

"""
w so writing and text is default, so WRITE HOGA AS TEXT 
append(a) means jodd dena, kisi text ko file ke end mein jodd dena

write mode ka matlab hota hai ki file mein jo kuch bhi likha hai use saaf krdo aur jo text de rhe hein, vo likh do
whereas,
append mode mein kisi bhi text ko file ke end mein joda jata hai
"""

