f = open("harshil2.txt")

print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(0)                 #seek is matlab reset kr diya
print(f.readline())
# print(f.tell())

f.close()